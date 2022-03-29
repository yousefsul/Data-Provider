import glob

from application.GlobalVariables import GlobalVariables
from bson import ObjectId

from consumer.consumer import Consumer
from consumer.consumer835 import Consumer835
from data_provider.data_provider_835 import DataProvider835
from process_files.ProcessFiles import ProcessFiles
from application.ConnectMongoDB import ConnectMongoDB
from mongodb_connection.ConnectMongoDBFinalReport import ConnectMongoDBFinalReport
from application.send_email.SendEmail import SendEmail

if __name__ == '__main__':
    mongo_client = "mongodb+srv://yousef:3h2rSzl0pPItpyGp@cluster0.umnlp.mongodb.net/client_2731928905_DB?retryWrites" \
                   "=true&w=majority"
    connection = ConnectMongoDB(database_name='client_2731928905_DB')
    connection.connect_to_collection('paymentsColl')
    # payments = connection.find_from_collection_by_key('header_section.current_status.status', 'new')
    payments = connection.find_from_collection()
    connection.connect_to_collection('835_dict_coll')
    master_payments = connection.find_from_collection()
    consumer = Consumer835("")
    consumer.check_credentials_code()
    # consumer.process_payment(payments, payment, connection.get_database_name())

    for payment in master_payments:
        consumer.process_payment(payments, payment, connection.get_database_name())
        payments.rewind()

    # consumer.create_final_reports(payments, master_payments, connection.get_database_name())

    # print(cursor)
    # print(x)
    # for i in cursor:
    #     print(i)
    #     print(i.get('header_section').get('trans_src_id'))
    #     if i.get('header_section').get('trans_src_id') == 1038391814:
    #         print(i)
    # consumer = Consumer("")
    # if consumer.check_credentials_code():
    #     process_999 = ProcessFiles()
    #     consumer.check_ack_file(process_999.get_edi_file(), process_999.get_ack_dict())
    # else:
    #     print("You Are Not Allowed to Access Data")
