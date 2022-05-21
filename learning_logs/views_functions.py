
def check_topic_owner(request, topic):
    if topic.owner != request.user:
        return False
    else:
        return True
