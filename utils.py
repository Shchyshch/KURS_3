import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row['description']
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        if 'from' in row:
            sender = row['from'].split()
            sender_account = sender.pop(-1)
            if len(sender_account) == 16:
                sender_account = f"{sender_account[:4]} {sender_account[4:6]}** **** {sender_account[-4:]}"
                sender_info = ' '.join(sender)
            else:
                sender_account = f"**{sender_account[-4:]}"
                sender_info = ' '.join(sender)
        else:
            sender_info, sender_account = '', ''
        recipient = row['to'].split()
        recipient_account = recipient.pop(-1)
        if len(recipient_account) == 16:
            recipient_account = f"{recipient_account[:4]} {recipient_account[4:6]}** **** {recipient_account[-4:]}"
            recipient_info = ' '.join(recipient)
        else:
            recipient_account = f"**{recipient_account[-4:]}"
            recipient_info = ' '.join(recipient)
        formatted_data.append(f'''\
{date} {description}
{sender_info} {sender_account} -> {recipient_info} {recipient_account}
{operations_amount}''')
    return formatted_data
