import os
import fire

from azure.storage.blob import BlockBlobService


def import_data_from_blob(account_name, account_key, container, data_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
    prefix_len = len(data_folder)
    for blob_path in blob_service.list_blob_names(container, prefix=data_folder):
        file_name = blob_path[prefix_len+1:]
        print(file_name)
        blob_service.get_blob_to_path(container_name=container, blob_name=blob_path, file_path=os.path.join(output_folder, file_name))
    pass


if __name__ == '__main__':
    fire.Fire(import_data_from_blob)