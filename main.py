from consumer.consumer import Consumer
from process_files.ProcessFiles import ProcessFiles

if __name__ == '__main__':

    consumer = Consumer("")
    if consumer.check_credentials_code():
        process_999 = ProcessFiles()
        consumer.check_ack_file(process_999.get_edi_file(), process_999.get_ack_dict())
    else:
        print("You Are Not Allowed to Access Data")
