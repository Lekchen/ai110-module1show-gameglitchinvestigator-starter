#understand:
# I:
# O:
# C:no constrains
# E:empty
#plan:start with initilizing the stacks, then loop through the comment list and append on to the stacks.
        #clear the comment list. pop everything in the stack and append it in the comment. retyurn the comments
#implement: 
def reverse_comments_queue(comments):
    stacks = list()
    for c in comments:
        stacks.append(c)
    comments.clear()
    while stacks:
        comments.append(stacks)
    return comments

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
