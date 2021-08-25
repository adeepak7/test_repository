from test_module_functions import *
import argparse
from timeit import default_timer as timer
import humanfriendly

start_time = timer()


parser = argparse.ArgumentParser()

# Required parameters

"""
The following 2 lines are overriding the optional group. Don't use it.
parser.add_argument('-message_from', metavar="message_from", type=str, help="Enter Sender's Name", required=True)
parser.add_argument('-input_message_file', metavar="input_message_file", type=str, help="Enter Sender's Message", required=True)
"""

required = parser.add_argument_group('required arguments')
required.add_argument('-msg_from', '--message_from', metavar="message_from", type=str, help="Enter Sender's Name", required=True)
required.add_argument('-inp_msg_file', '--input_message_file', metavar="input_message_file", type=str, help="Enter Sender's Message", required=True)


# Optional parameters

parser.add_argument("-v", "--verbose",
                    action="store_true",
                    help="increase output verbosity")

parser.add_argument("-o", "--output_file_name",
                    metavar="output_file_name",
                    help="Enter output file name")


args = parser.parse_args()

if args.verbose:
    print('Verbose enabled!')

print('------------------------------------')
print('Following arguments were passed:')
print(args)
print('------------------------------------')

# Testing arguments
print(args.message_from)
print(args.input_message_file)

output_file_name = args.output_file_name
print(type(output_file_name))

if type(output_file_name) == type(None) or output_file_name == '':
    output_file_name = 'output.txt'

if not output_file_name.endswith('.txt'):
        output_file_name = output_file_name + '.txt'

input_file = open(args.input_message_file)

with open(output_file_name, 'w') as out:
    out.write("To: The Mesirov's Lab \nFROM: {sender} \nMESSAGE: {message}".format(sender=args.message_from, message=input_file.readline()))

out.close()

end_time = timer()

print('Task Completes in {time}'.format(time = humanfriendly.format_timespan(end_time - start_time)))



