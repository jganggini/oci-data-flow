from src.parameters import *
from src.oci_autonomous_database import oci_autonomous_database
import argparse

parser  = argparse.ArgumentParser()
parser.add_argument('-d', "--delete", type=int, help="Eliminar un registro")
args = vars(parser.parse_args())

def main():
    try:
        if int(args['delete']) > 0:
            print("# Delete object(s) from Autnomous Database...")
            oci_autonomous_database.delete_row('DEMO_CUSTOMERS', 'CUST_ID', args['delete'])
       
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # create Spark context with Spark configuration
    main()
