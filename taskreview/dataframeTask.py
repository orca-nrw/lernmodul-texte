from IPython.core.display import display

from taskreview.task import Task

class PandasDataframeTask(Task):
    """
    A class used to represent a dataframe task

    ...

    Attributes
    ----------


    Methods
    -------
    check_solution(button)
        Checks the solution when the check button is clicked
    evaluate_task(df)
        Evaluates the task based on the submitted solution
    """

    def __init__(self, db_conn, task_id):
        super().__init__(db_conn, task_id)
    
    def check_solution(self, button):
        """Checks if the solution of the user is correct

        Parameters
        ----------
        button: Button
            Button that has been clicked to execute this method
        """

        if self.solution.equals(self.user_solution):
            self.is_task_answered_correctly = True
            self.display_img_correct()
            self.display_disabled_buttons()
        else:
            self.get_specific_error_evaluation()
            
            # increment counter of tries
            self.cnt_false_answers.increment()
                
            if self.cnt_false_answers.get_value() >= 3:
                self.display_solution_btn()     
                
    def get_specific_error_evaluation(self):
        """Gets a more speficic evaluation of the task if the user solution is not correct. Various
         things are evaluated: number of columns, number of rows, column names, sorting of columns, ...
        """
            
        # check number of cols
        num_cols_correct = self.check_num_cols_rows(1)
        # check the number of rows
        num_rows_correct = self.check_num_cols_rows(0)
        # check the column names
        col_names_correct = self.check_col_names() 
        # check sorting of columns
        col_sorting_correct = self.check_col_sorting()
        # check if the content of cells is correct
        cell_content_correct = self.check_cell_content()
        
        evaluation_txt = "Leider ist die Eingabe nicht korrekt. Bitte versuche es erneut!<br> Auswertung der Überprüfung:<ul>"
        
        if not num_cols_correct:
            evaluation_txt += "<li>Die Anzahl der Spalten stimmt nicht.<br></li>"
        
        # only check sorting if the number of rows is correct. Otherwise sorting is false every time
        # only check content if sorting is correct. Otherwise content is also false every time
        if not num_rows_correct:
            evaluation_txt += "<li>Die Anzahl der Zeilen stimmt nicht.<br></li>"
        elif not col_sorting_correct:
            evaluation_txt += "<li>Die Sortierung der Spalten stimmt nicht.<br></li>"
        elif not cell_content_correct:
            evaluation_txt += "<li>Der Zellinhalt des DataFrames stimmt nicht.<br></li>"
            
        if not col_names_correct:
            evaluation_txt += "<li>Die Spaltennamen stimmen nicht.<br></li>"
            
        evaluation_txt += "<ul>"    
        self.display_text(evaluation_txt)
        
        
    def check_num_cols_rows(self, shape_index):
        """Checks if the amount of rows and columns is correct

        Parameters
        ----------
        shape_index : int
            index of the rows (0) or the cols (1) 
            
        Returns
        -------
        Boolean
            if the number of cols or rows of the user is correct
        """
        
        sol_num = self.solution.shape[shape_index]
        user_num = self.user_solution.shape[shape_index]
        
        return sol_num == user_num
        
        
    def check_col_names(self):
        """Checks if the column names of the user dataframe are correct
            
        Returns
        -------
        Boolean
            if the column names of the user dataframe are correct
        """
        
        sol_col_names = self.solution.columns.values
        user_col_names = self.user_solution.columns.values
        user_col_names_list = user_col_names.tolist()
        
        for name in user_col_names:
            if name in sol_col_names:
                user_col_names_list.remove(name)
        
        return not user_col_names_list 
    
    def get_num_equal_cols(self):
        """Gets the number of equal cells between the user dataframe and the solution dataframe
            
        Returns
        -------
        int
            number of equal cells
        """
        
        correct_cols = 0
        
        for name in self.solution.columns.values:
            if name in self.user_solution.columns.values:
                if self.user_solution[name].equals(self.solution[name]):
                    correct_cols += 1
                    
        return correct_cols
    
    def check_col_sorting(self):
        """Checks if the columns are sorted correctly
            
        Returns
        -------
        Boolean
            if the columns are sorted correctly
        """
        correct_cols = self.get_num_equal_cols()
                
        return correct_cols > (len(self.user_solution.columns) - correct_cols)
    
    def check_cell_content(self):
        """Checks if the content of cells is correct
            
        Returns
        -------
        Boolean
            if the content of cells is correct
        """
        correct_cols = self.get_num_equal_cols()
        
        sol_col_names = self.solution.columns.values
        user_col_names = self.user_solution.columns.values
        
        wrong_col_names = len(sol_col_names)
        
        for name in sol_col_names:
            if name in user_col_names:
                wrong_col_names -= 1
        
        return (len(self.solution.columns) - correct_cols - wrong_col_names) == 0
            
            
    def evaluate_task(self, df):
        """Makes it possible to evaluate the task by displaying the buttons. Display user solution.

        Parameters
        ----------
        df : pandas.DataFrame
            Dataframe that the user submitted
        """

        display(df)
        self.user_solution = df
        self.display_buttons()




class SparkDataframeTask(PandasDataframeTask):
    """
    A class used to represent a spark dataframe task

    ...

    Attributes
    ----------


    Methods
    -------
    evaluate_task(df)
        Evaluates the task based on the submitted solution
    """

    def __init__(self, db_conn, task_id):
        super().__init__(db_conn, task_id)

    def evaluate_task(self, df):
        """Makes it possible to evaluate the task by displaying the buttons. Shows user solution as spark dataframe.

        Parameters
        ----------
        df : pyspark.sql.DataFrame
            Dataframe that the user submitted
        """

        df.show()
        self.user_solution = df.toPandas()
        self.display_buttons()