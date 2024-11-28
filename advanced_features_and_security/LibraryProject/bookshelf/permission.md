# First create a custom permission in the book model with a meta sub class
# Permissions include can_edit, can_create can_view, can_delete
# Next create the custom groups "Admins, Viewers, Editors" from shell using the command below
# Group.objects.get_or_create(name="Viewers")
# Assign the permissions to the groups using: group_name.permissions.add(permission)
# Next create the users with different roles and assign them to vvarious groups
# Create different routes for creat, edit, view and delete as well as book_list
# use the permission_required decorator to restrict access to only users that have the particular permission
# In the templates also validate the permission using {% if perms.users.can_view%} display the appropriate view for the user
# Also as an additional step if the user tries to access the view without authenticating send them to the login page this is also achieve with the @login_required decorator