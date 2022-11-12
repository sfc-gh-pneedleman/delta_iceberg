import csv
from pathlib import Path
from zipfile import ZipFile, ZIP_BZIP2

from generators import TYPES_TO_GENERATORS
from schemas import CUSTOMERS_SCHEMA, TXN_SCHEMA, ORGANIZATIONS_SCHEMA

SCHEMA_TO_DICT = {
    'customers': CUSTOMERS_SCHEMA,
    'txn': TXN_SCHEMA,
    'organizations': ORGANIZATIONS_SCHEMA
}


def generate_file(schema='customers', name="customers", count=1000000):
    p = Path(__file__).parent / "../csv_files/{}".format(schema)
    p.mkdir(parents=True, exist_ok=True)

    file_name = "{}.csv".format(name)
    file_path = p / file_name

    if not file_path.exists():
        schema_dict = SCHEMA_TO_DICT[schema]

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # Headers
            headers = [elem['name'] for elem in schema_dict]
            headers.insert(0, "ID") # Add an Index header
            writer.writerow(headers)

            # Content
            data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]

            rows = []
            for index in range(1, count+1):
                row = [gen() for gen in data_generators]
                row.insert(0, index)
                rows.append(row)

                if index % 100000 == 0:
                    writer.writerows(rows)
                    rows = []

                if index % 100000 == 0:
                    print("{}/{}".format(index, count))

            writer.writerows(rows)
    else:
        print("{} already exists".format(file_path))

    # Create a index version
    #file_name_zip = "{}.zip".format(name)
    #file_path_zip = p / file_name_zip
    #if not file_path_zip.exists():
    #    with ZipFile(file_path_zip, 'w', ZIP_BZIP2) as zipObj:
    #        zipObj.write(filename=file_path, arcname=file_name)




if __name__ == '__main__':
    generate_file('customers', 'customers-5M', 5000000)                                               

    generate_file('txn', 'txn-100M', 100000000)                                     