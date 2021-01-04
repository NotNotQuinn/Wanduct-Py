import logging

# I stole this from stackoverflow, but I added tags parsing

class IRCBadMessage(BaseException):
    pass

def parsemsg(s) -> (str, str, list):
    """Breaks a message from an IRC server into its prefix, command, and arguments.

    Returns: prefix, command, args, tags
    """
    tags_out = {}
    prefix = ''
    trailing = []
    if s.startswith("@"):  # if there is tags
        (tags, s) = s.split(' ', 1)  # remove the tags from the message, and let the rest of the program work as intended without them
        tags = tags[1:]  # remove the @ at the beginning
        tags = tags.split(';')  # seperates individual tags into a list of strings ex: "badges=moderator/1"
        for tag in tags:  
            (key, value)  = tag.split('=', 1)  #get the keys and set them to there values
            if value == '': value = True  # when a tag is present, but has no value, set it to true (because an empty string reads as false)
            tags_out[key] = value 

    if not s:
       raise IRCBadMessage("Empty line.")
    if s[0] == ':':
        prefix, s = s[1:].split(' ', 1)
    if s.find(' :') != -1:
        s, trailing = s.split(' :', 1)
        args = s.split()
        args.append(trailing)
    else:
        args = s.split()
    command = args.pop(0)
    return prefix, command, args, tags_out
