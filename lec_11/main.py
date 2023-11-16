import requests

base_url = 'https://jsonplaceholder.typicode.com'
posts = requests.get(f'{base_url}/posts').json()
filtered_titles = [{'userId':post_dict['userId'],'id':post_dict["id"]} for post_dict in posts if len(post_dict['title'].split()) <= 6]

# print(posts)
print("---------Titles with 6 or fewer words---------")
print(filtered_titles)



filtered_bodies = [post_dict for post_dict in posts if len(post_dict['body'].split('\n')) <= 3]

print("\nPosts with 3 or fewer lines in the body:")
for post in filtered_bodies:
    print(f"Title: {post['title']}\nBody:\n{post['body']}\n")





new_post = {
    'userId': 1,
    'title': 'New Post Title',
    'body': 'New post body content'
}
created_post = requests.post(f'{base_url}/posts', json=new_post).json()
print("\nCreated Post:")

post_to_update_id = 1
updated_post = {
    'title': 'Updated Title',
    'body': 'Updated body content'
}
requests.put(f'{base_url}/posts/{post_to_update_id}', json=updated_post)


# DELETE request to delete a post
post_to_delete_id = 1
requests.delete(f'{base_url}/posts/{post_to_delete_id}')

# Confirm deletion by trying to fetch the deleted post
deleted_post = requests.get(f'{base_url}/posts/{post_to_delete_id}')
print("deleted_post status_code: ", deleted_post.status_code)  # Should print 404