# Django Group and Permission Management

## Overview
This project implements role-based access control using Django's permission system.

## Features
- **Custom Permissions** for the `Book` model.
- **Groups**:
  - `Viewers` (can view books)
  - `Editors` (can view, create, edit books)
  - `Admins` (can view, create, edit, delete books)
- **Views with Permission Checks** using `@permission_required`.

## Setup Instructions
1. **Run Migrations**

