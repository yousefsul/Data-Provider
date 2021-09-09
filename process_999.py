from connectMongoDB import ConnectMongoDB


class Process_999:
    def __init__(self):
        self.connection = ConnectMongoDB()
        self.__db_name = self.connection.get_database_name()
        self.unproccessed_files = None
        self.unproccessed = None
        self.ack_dict = None
        self.segment_ack_dict = None
        self.segment_unprocessed = None
        self.file_rejected = False
        self.__find_unproccessed_files()

    def __find_unproccessed_files(self):
        self.connection.connect_to_837_collection()
        self.unproccessed_files = self.connection.get_unproccessed_files()
        for self.unproccessed in self.unproccessed_files:
            self.__get_ack()
            # self.__start_processing()

    def __get_ack(self):
        self.connection.connect_to_ack_collection()
        self.ack_dict = self.connection.get_ack_dict(self.unproccessed.get('header_section').get('trans_src_id'))
        self.ack_dict['database_name'] = self.__db_name

    def __start_processing(self):
        for self.segment_ack_dict in self.ack_dict:
            if self.segment_ack_dict.split('-')[0] == 'AK2':
                for self.segment_unprocessed in self.unproccessed:
                    if self.segment_unprocessed.split('-')[0] == 'ST':
                        if self.ack_dict.get(self.segment_ack_dict).get('02') == self.unproccessed.get(
                                self.segment_unprocessed).get('02'):
                            pass
                            break

    def __update_file_status(self):
        if self.file_rejected:
            self.connection.update_file_status(self.unproccessed.get('_id'))
            self.connection.update_file_status_history(self.unproccessed.get('_id'))

    def get_ack_dict(self):
        return self.ack_dict

    def get_edi_file(self):
        return self.unproccessed
