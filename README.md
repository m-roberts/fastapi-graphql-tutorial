# FastAPI / GraphQL Tutorial

https://testdriven.io/blog/fastapi-graphql/

Note: The actual GraphQL integration here is out of date - it is [no longer provided via Starlette](https://www.starlette.io/graphql/) (FastAPI dependency).

## Queries

Create a "John Doe" user:
```
mutation createUser {
  createUser(userDetails: {
    name: "John Doe",
    address: "Some address",
    phoneNumber: "12345678",
    sex: "male"
  })
  {
    id
    name
    posts {
      body
      comments {
        body
      }
    }
  }
}
```

Create a post for John Doe:
```
mutation createPost {
  createPost(postDetails: {
    userId: 1,
    title: "My first Post",
    body: "This is a Post about myself"
  })
  {
    id
  }
}
```

Create a comment on the post:
```
mutation createComment {
  createComment(commentDetails: {
    userId: 1,
    postId: 1,
    body: "Another Comment"
  })
  {
    id
    body
  }
}
```

List all users:
```
query getAllUsers {
  listUsers {
    id
    name
    posts {
      title
    }
  }
}
```

Get a specific user by ID:
```
query getUser {
  getSingleUser(userId: 1) {
    name
    posts {
      title
      comments {
        body
      }
    }
    comments {
      body
    }
  }
}
```
