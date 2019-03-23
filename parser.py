import csv
import json

source_data = open('driver_registration.csv')
json_data = open('driver_registration.json', 'w')

field_names = ["id", "date_created", "date_last_modified", "active_date", "name", "phone", "resign_date", "resign_reason", "status", "tipe", "area", "CONCAT(operator_,'id')", "modified_by", "vehicle_type", "helmet_qty", "jacket_qty", "vehicle_brand", "vehicle_year", "bike_type", "first_ride_bonus_awarded", "is_doc_completed"]

data_read = csv.DictReader(source_data, field_names)

for row in data_read:
    json.dump(row, json_data)
    json_data.write('\n')