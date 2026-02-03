# example-data

This repository contains example JSON files with various data structures for testing, learning, and data analysis purposes.

## Example Data Files

### Simple Data Structures
- **simple_user.json** - Basic user profile with minimal fields
- **product.json** - Product information with common e-commerce fields
- **users_list.json** - Array of user objects with roles and timestamps

### Complex Nested Data
- **company_structure.json** - Multi-level organizational hierarchy with departments and teams
- **ecommerce_order.json** - Detailed order with customer, items, shipping, and payment information
- **weather_data.json** - Weather data with current conditions and forecast
- **blog_posts.json** - Blog posts with authors, tags, and nested comments
- **restaurant_menu.json** - Restaurant menu with categorized items and detailed attributes
- **library_catalog.json** - Library book catalog with availability information
- **sports_team.json** - Sports team roster with player statistics
- **movie_database.json** - Movie information with cast, crew, and box office data

### AWS Boto3 Response Examples
- **boto3_ec2_describe_instances.json** - AWS EC2 describe_instances() response with multiple running instances
- **boto3_ec2_describe_security_groups.json** - AWS EC2 describe_security_groups() response with various security group configurations

## Exercises

The **exercises/** directory contains Python programming exercises for learning AWS boto3:
- **Boto3 EC2 Exercises** - Hands-on exercises for working with AWS EC2 using boto3
  - Counting running instances
  - Creating new EC2 instances
  - Retrieving external IP addresses
  - Each exercise includes a matching solution file

See [exercises/README.md](exercises/README.md) for detailed instructions.

## Usage

These JSON files can be used for:
- Learning JSON structure and parsing
- Testing data processing scripts
- Practicing data analysis with Python, JavaScript, or other languages
- Understanding AWS API responses
- Developing and testing applications that consume JSON data
- Practicing boto3 exercises with realistic AWS response data

## File Complexity Levels

- **Simple** (1-10 fields): simple_user.json, product.json
- **Medium** (10-50 fields): users_list.json, weather_data.json, library_catalog.json
- **Complex** (50+ fields): company_structure.json, ecommerce_order.json, restaurant_menu.json, sports_team.json, blog_posts.json, movie_database.json
- **AWS API Responses**: boto3_ec2_describe_instances.json, boto3_ec2_describe_security_groups.json