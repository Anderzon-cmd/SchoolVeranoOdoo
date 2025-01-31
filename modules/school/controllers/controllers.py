# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

from odoo.http import request
from odoo import http


class School(http.Controller):

    # @http.route('/school/school',auth='public',type='http',website=True)
    # def handler(self):
    #     print(self)
    #     print('hola mundo')
    #     return 'Hello world'
    @http.route('/module/school/students', auth='public',type='http',website=True,methods=['GET'])
    def index(self, **kw):
        students = request.env['school.student'].sudo().search([])
         #return str(students[0].name)
         #return request.render('school.student_tree_view',{'students':students})
         #print(students)   
         #Datos de ejemplos
        df_notes=pd.DataFrame({
            'Asistencia':[85,60,90,40,75],
            'Evaluaciones':[78,55,95,50,80],
            'Actividades':[92,65,85,45,70],
            'Tarea':[88,70,90,50,75],
            'Estado':[1,0,1,0,1]
        });
        print("Cantidad de estudiantes encontrados:", len(students))    
        #Separar caracteristicas y variable objetivo
        X=df_notes[[
            'Asistencia',
            'Evaluaciones',
            'Actividades',
            'Tarea',
        ]]
        y=df_notes['Estado']    
        #Crear y entrenar el modelo 
        model = RandomForestClassifier(random_state=42)
        model.fit(X,y)  
        #Guardar el modelo en un archivo
        #joblib.dump(model,)    
        path_current=os.getcwd()
        joblib.dump(model,os.path.join(path_current,'modules','school','model_training','random_forest_clasifier','model.pkl')) 
        print(X)
        print(y)
        print(df_notes);

        return http.request.render('school.school_template', {'students': http.request.env['school.student'].search([])})

#     @http.route('/school/school/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school.listing', {
#             'root': '/school/school',
#             'objects': http.request.env['school.school'].search([]),
#         })

#     @http.route('/school/school/objects/<model("school.school"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school.object', {
#             'object': obj
#         })
    @http.route('/module/school/students', auth='public',type='http',website=True,methods=['POST'], csrf=True)
    def predicting(self, **kw):
        path_current=os.getcwd()
        model=joblib.load(os.path.join(path_current,'modules','school','model_training','random_forest_clasifier','model.pkl'))
        new_note=np.array([[40,50,10,10]])
        prediction=model.predict(new_note)
        
        return http.request.render('school.school_predicting', {'predicting': prediction})


        
    

