
Class Moderators(User):
    """This python module defines moderator access.  """
    def remove_comment(comment_id):
        """The moderator can delete inappropriate comments after identifying their id"""
        del comment_list[comment_id]
        return comment_list
