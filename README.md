# FastAPI / GraphQL Tutorial

This is a completed version of [`testdriven.io`'s FastAPI+GraphQL blog tutorial](https://testdriven.io/blog/fastapi-graphql/), with the latest versions of the relevant dependencies (at time of publishing).

The original blog post was using GraphQL provided directly with Starlette (a FastAPI dependency), which [now requires a third-party library](https://www.starlette.io/graphql/). [`starlette-graphene3`](https://github.com/ciscorn/starlette-graphene3) provides the mechanism for connecting `graphene` with `starlette` which was removed from `starlette` (`GraphQLApp`).

## Example GraphQL Queries

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
