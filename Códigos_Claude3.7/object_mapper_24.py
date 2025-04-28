class ObjectMapper:
    def map_to_object(self, data_dict, model_class):
        """
        Maps a dictionary to a specified Python object based on the provided model class.
        
        :param data_dict: Dictionary containing data to be mapped.
        :param model_class: The class of the object to be created.
        :return: An instance of the model_class populated with data from data_dict.
        """
        return model_class(**data_dict)