# -*- coding: utf-8 -*- 
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import os
import time
import hashlib
import cPickle

def index():
    """
    Test powerTable
    """
    RUNQUERYPATH = "../master/code/runQuery/"
    session.data = []
    session.query = ""
    logfile = open('logs/'+str(response.session_id),'a')
    logfile.write("SESSION: "+str(response.session_id)+"\n")
    logfile.write("TIME: "+time.strftime("%X %x %z")+"\n")
    db.t_result.truncate()
    db.t_resdis.truncate()
    query = ""
    collection = ""
    diseases = ""
    reranking = ""
    timer = ""
    table = ""
    distable = ""
    if request.vars.q:
        t0 = time.clock()
        query = request.vars.q
        checked = request.vars.c
        os.system('pwd')
        if checked == "on":
            hashstring = hashlib.md5(request.vars.q+"index_raregenet"+str(time.time())).hexdigest()
            collection = "CHECKED"
            if request.vars.dis == "on" or request.vars.rer == "on":
                if request.vars.dis == "on":
                    os.system('sh '+RUNQUERYPATH+'runQueryDiseases.sh "'+request.vars.q+'" index_raregenet '+hashstring)
                    diseases = "CHECKED"
                if request.vars.rer == "on":
                    os.system('sh '+RUNQUERYPATH+'runQueryReranked.sh "'+request.vars.q+'" index_raregenet '+hashstring)
                    reranking = "CHECKED"
            else:
                os.system('sh '+RUNQUERYPATH+'runQuery.sh "'+request.vars.q+'" index_raregenet '+hashstring)
        else:
            hashstring = hashlib.md5(request.vars.q+"index_rare"+str(time.time())).hexdigest()
            collection = ""
            if request.vars.dis == "on" or request.vars.rer == "on":
                if request.vars.dis == "on":
                    os.system('sh '+RUNQUERYPATH+'runQueryDiseases.sh "'+request.vars.q+'" index_rare '+hashstring)
                    diseases = "CHECKED"
                if request.vars.rer == "on":
                    os.system('sh '+RUNQUERYPATH+'runQueryReranked.sh "'+request.vars.q+'" index_rare '+hashstring)
                    reranking = "CHECKED"
            else:
                os.system('sh '+RUNQUERYPATH+'runQuery.sh "'+request.vars.q+'" index_rare '+hashstring)
        db.t_result.truncate()
        db.t_result.import_from_csv_file(open(os.getcwd()+'/results/'+hashstring,'r'))
        for row in db().select(db.t_result.ALL):
            session.data.append([row.f_title,row.f_url,row.f_snippet])
        session.hashstring = hashstring
        session.query = query
        if request.vars.dis == "on":
            db.t_resdis.truncate()
            db.t_resdis.import_from_csv_file(open(os.getcwd()+'/results/'+hashstring+'.dis','r'))
        timer = time.clock() - t0
        logfile.write("QUERY: "+query+"\n")
        logfile.write("GENETIC CHECKED: "+str(checked)+"\n")
        logfile.write("RESULT FILE: "+hashstring+"\n")
        logfile.write("SECONDS: "+str(timer)+"\n")
        logfile.close()
        table = createResultTable(db.t_result)
        if request.vars.dis == "on":
            #distable = createDiseaseTable(db.t_resdis)
            distable = SQLTABLE(db().select(db.t_resdis.f_rank,db.t_resdis.f_disease,db.t_resdis.f_freq,db.t_resdis.f_docnos),headers='labels',truncate=80)
        timer = str(timer)[:5] + " seconds"
        print timer
    return locals()
    
def createResultTable(data):
    class Virtual(object):
        @virtualsettings(label=T('Source'))
        def sourcelink(self):
            return A(self.t_result.f_source,_href=self.t_result.f_url,_target='_blank')
    
    table = plugins.powerTable
    table.datasource = data
            
    table.dtfeatures['sScrollY'] = '100%'
    table.virtualfields = Virtual()
    table.dtfeatures['bSort'] = False
    table.dtfeatures['aaSortingFixed'] = [[2,'asc']]
    table.dtfeatures['iDisplayLength'] = 20
    table.dtfeatures['bPaginate'] =  False
    
    table.truncate = 60 
    table.headers = 'labels'
    table.keycolumn = 't_result.id'
    table.showkeycolumn = False
    table.extra = dict(
                       details={'detailscolumns':'t_result.f_title,t_result.f_url,t_result.f_snippet','detailscallback':URL('display_details.load')}
                       )
    table.columns = ['t_result.f_rank',
                     't_result.f_title',
                     'virtual.sourcelink',
                     #'t_result.f_source',
                     #'t_result.f_docno',
                     #'t_result.f_score',
                    ]
    table.hiddencolumns = ['t_result.f_source','t_result.f_url']
    table.dtfeatures['bInfo'] =  False
    table.dtfeatures['bFilter'] =  False
    table.dtfeatures['bAutoWidth'] =  False
    table.dtfeatures['aoColumns'] = [
            { 'sWidth': '0%' },
            { 'sWidth': '5.5%' },
            { 'sWidth': '5.5%' },
            { 'sWidth': '55.5%' },
            { 'sWidth': '33.5%' }
        ]
    return table.create()

def createDiseaseTable(data):
    distable = plugins.powerTable
    distable.datasource = data
    
    distable.dtfeatures['sScrollY'] = '100%'
    distable.dtfeatures['bSort'] = False
    distable.dtfeatures['aaSortingFixed'] = [[2,'asc']]
    distable.dtfeatures['iDisplayLength'] = 20
    distable.dtfeatures['bPaginate'] =  False
    distable.dtfeatures['bInfo'] =  False
    distable.dtfeatures['bFilter'] =  False
    
    distable.truncate = 60 
    distable.headers = 'labels'
    distable.keycolumn = 't_resdis.id'
    distable.showkeycolumn = False
    
    distable.columns = ['t_resdis.f_rank',
                     't_resdis.f_disease',
                     't_resdis.f_freq',
                     't_resdis.f_docnos',
                     ]
                     
    return distable.create()

def filterOnString(fs):
        fs = fs.lower()
        query = (db.t_result.f_title.lower().contains(fs) | db.t_result.f_snippet.lower().contains(fs) | db.t_result.f_source.lower().contains(fs) ) 
        return db(query).select()
 
def display_details():
    """
    return a custom object to be inserted in detail for table
    """
    key = None
    cols = None
    for k in request.vars.keys():
        if k[:3] == 'dt_':
            key = request.vars[k]
        elif k[:6] == 'dtcols':
            cols = request.vars[k]

    value = int(key.split('.')[2])
    rows = cPickle.load(response.session_file)['data']
    row = rows[value-1]

    logfile = open('logs/'+str(response.session_id),'a')
    logfile.write("OPENED DETAILS FOR RANK: "+str(value)+"\n")
    logfile.close()
    
    details = DIV(B("Title: "))
    details.append(P(str(row[0])))
    details.append(B("URL: "))
    details.append(P(A(str(row[1]),_href=str(row[1]),_target='_blank')))
    details.append(B("Text: "))
    details.append(P(str(row[2])))
    return details

def feedback():
    if request.vars.comment:
        feedbackfile = open("logs/messages","a")
        feedbackfile.write("SESSION: "+str(response.session_id)+"\n")
        feedbackfile.write("TIME: "+time.strftime("%X %x %z")+"\n")
        if session.query:
            feedbackfile.write("QUERY: "+str(session.query)+"\n")
        if session.hashstring:
            feedbackfile.write("RESULT FILE: "+str(session.hashstring)+"\n")
        else:
            feedbackfile.write("RESULT FILE: "+"no recent queries"+"\n")
        if response.session_id:
            feedbackfile.write("LOG FILE: "+str(response.session_id)+"\n")
        feedbackfile.write("COMMENT: '"+str(request.vars.comment)+"'\n")
        feedbackfile.close()
        message="Feedback received. Thank you!"
        return message
    return ""

def filterResults():
    fword = str(request.vars.values()[0])
    data = filterOnString(fword)
    table = createResultTable(data)
    return str(table) + "<script>addFilterBox('"+str(fword)+"');$('input#fword').focus().val($('input#fword').val());</script>"

def user():
    """
    exposes:
    http://..../[app]/default/user/login 
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()
