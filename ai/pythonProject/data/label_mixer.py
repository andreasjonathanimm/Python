import os
import csv
import json

def mix_labels(labelme_dir, output_csv):
    # Get all labelme files in the directory
    labelme_files = [f for f in os.listdir(labelme_dir) if f.endswith('.json')]

    # Create the CSV file and write the header
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image', 'Label', 'Xmin', 'Ymin', 'Xmax', 'Ymax'])

        # Process each labelme file
        for labelme_file in labelme_files:
            # Parse the labelme file and extract the labels
            # Replace this with your own code to parse the labelme file
            image_name = labelme_file[:-5] + '.jpg'
            labels = parse_labelme_file(os.path.join(labelme_dir, labelme_file))

            # Write the labels to the CSV file
            for i in range(len(labels['class'])):
                writer.writerow([image_name, labels['class'][i], labels['xmin'][i], labels['ymin'][i], labels['xmax'][i], labels['ymax'][i]])

def parse_labelme_file(labelme_file):
    # Replace this with your own code to parse the labelme file
    # and extract the labels for each object
    labels = {'class': [], 'xmin': [], 'ymin': [], 'xmax': [], 'ymax': []}
    with open(labelme_file) as f:
        data = json.load(f)
        for shape in data['shapes']:
            labels['class'].append(shape['label'])
            labels['xmin'].append(shape['points'][0][0])
            labels['ymin'].append(shape['points'][0][1])
            labels['xmax'].append(shape['points'][1][0])
            labels['ymax'].append(shape['points'][1][1])
    
    return labels

# Usage example
labelme_dir = './barcode-and-qr/labels'
output_csv = './barcode-and-qr/labels.csv'
mix_labels(labelme_dir, output_csv)