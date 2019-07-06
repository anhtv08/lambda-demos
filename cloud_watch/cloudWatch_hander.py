


def lambda_handler(event, context):
    print(context)

    # queue_url_endpoint = context['client_context']['evn']['queue_ur']
    # print("passing queue_url from context:" + queue_url_endpoint)
    records = event['Records']
    return generate_signed_urls(records)
