from argparse import ArgumentParser

import pysam


def merge(input_path, output_path, custom_id='custom_id', line_length=80):
    with open(output_path, 'w+') as out_f:
        out_f.write(f'>{custom_id}\n')
        data = ''
        with pysam.FastxFile(input_path) as in_f:
            for record in in_f:
                print(f'Merging {record.name}')
                data += record.sequence
                for i in range(0, len(data), line_length):
                    chunk = data[i:i + line_length]
                    if len(chunk) == line_length:
                        out_f.write(chunk+'\n')
                    else:
                        data = chunk
        if len(data) > 0: out_f.write(data+'\n')

def main():
    parser = ArgumentParser(description='FASTA-merge: merge multiple FASTA sequences into one')

    parser.add_argument('input_path', type=str,
                        help='str: input FASTA file')
    parser.add_argument('output_path', type=str,
                        help='str: output FASTA file')
    parser.add_argument('custom_id', type=str,
                        help='str: custom id for the resulting single sequence')
    parser.add_argument('line_length', type=int, nargs='?',
                        help='int: line length (default=80)')

    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    custom_id = args.custom_id
    line_length = args.line_length
    if line_length == None: line_length = 80

    merge(input_path, output_path, custom_id=custom_id, line_length=line_length)

if __name__ == '__main__':
    main()
