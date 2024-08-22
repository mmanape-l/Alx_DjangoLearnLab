# Permissions and Groups Setup

## Custom Permissions

The following permissions have been defined for the `Book` model:
- `can_view`: Allows viewing of books.
- `can_create`: Allows creation of books.
- `can_edit`: Allows editing of books.
- `can_delete`: Allows deletion of books.

## Groups and Permissions

### Groups
- **Editors**: Can create and edit books.
- **Viewers**: Can view books.
- **Admins**: Can view, create, edit, and delete books.

## Views Protection

The following views enforce permissions:
- `book_list`: Requires `can_view` permission.
- `book_create`: Requires `can_create` permission.
- `book_edit`: Requires `can_edit` permission.
- `book_delete`: Requires `can_delete` permission.
