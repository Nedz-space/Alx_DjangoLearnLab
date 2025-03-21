# Blog Post CRUD Features

## Functionality
- **ListView** (`/posts/`): View all posts.
- **DetailView** (`/posts/<id>/`): View post details.
- **CreateView** (`/posts/new/`): Authenticated users create posts.
- **UpdateView** (`/posts/<id>/edit/`): Only the post's author can edit.
- **DeleteView** (`/posts/<id>/delete/`): Only the post's author can delete.

## Permissions
- Only logged-in users can create, edit, or delete posts.
- Unauthenticated users can browse post listings and details.

## Templates
- `post_list.html`, `post_detail.html`, `post_form.html`, `post_confirm_delete.html`

## Setup
- Make sure to apply migrations: `python manage.py makemigrations` and `migrate`
- Start the server: `python manage.py runserver`


## Tagging and Search Features

### Adding Tags to Posts
- Create or edit a post.
- Enter tags in the "Tags" field. Separate tags with commas.

### Viewing Posts by Tag
- Click on any tag displayed in the post detail view.
- You will be redirected to a page listing all posts with that tag.

### Searching Posts
- Use the search bar to look for posts.
- You can search by title, content, or tags.

