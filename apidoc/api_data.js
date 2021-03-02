define({ "api": [
  {
    "type": "POST",
    "url": "/api/social/like/create/",
    "title": "Create like",
    "name": "Create_like",
    "group": "Like",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "post",
            "description": "<p>Post id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user",
            "description": "<p>User id</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "liked",
            "description": "<p>Is post liked or unliked?</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "like",
            "description": "<p>Id of created like</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "apidoc_rules/like.py",
    "groupTitle": "Like"
  },
  {
    "type": "GET",
    "url": "/api/social/analytics/",
    "title": "Get like stats",
    "name": "Get_like_stats",
    "group": "Like",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "optional": false,
            "field": "begin_date",
            "description": "<p>Start range date</p>"
          },
          {
            "group": "Parameter",
            "optional": false,
            "field": "end_date",
            "description": "<p>End range date</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "stats",
            "description": "<p>Grouped by date amount of likes</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"stats\": [\n    {\n        \"added_date\": \"2021-03-01\",\n        \"dcoun\": 1\n    },\n    {\n        \"added_date\": \"2021-03-02\",\n        \"dcoun\": 196\n    }\n]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc_rules/like.py",
    "groupTitle": "Like"
  },
  {
    "type": "POST",
    "url": "/api/social/post/create/",
    "title": "Create post",
    "name": "Create_post",
    "description": "<p>Create post</p>",
    "group": "Post",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user_id",
            "description": "<p>Id user</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Post name</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "post",
            "description": "<p>Id of created post</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"post\": 209\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc_rules/post.py",
    "groupTitle": "Post"
  },
  {
    "type": "GET",
    "url": "/api/social/post/{pk}",
    "title": "Get post",
    "name": "Get_post",
    "description": "<p>Get post</p>",
    "group": "Post",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>Post id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id of created post</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Post name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>Link to post image file</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "description",
            "description": "<p>Post description</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"name\": \"twet\",\n    \"image\": \"http://127.0.0.1:8000/media/PHZ_0733.jpg\",\n    \"description\": \"\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc_rules/post.py",
    "groupTitle": "Post"
  },
  {
    "type": "POST",
    "url": "/api/social/user/get-profile/{pk}",
    "title": "Get profile",
    "name": "Get_profile",
    "group": "User",
    "description": "<p>Get profile</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>User id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Id of got user</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>user name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "login",
            "description": "<p>user login</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>user password</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_login",
            "description": "<p>last login time</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_request",
            "description": "<p>last request time</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"name\": \"test\",\n    \"login\": \"test1\",\n    \"password\": \"test-pass\",\n    \"last_login\": \"08:41:36.374845\",\n    \"last_request\": \"15:17:23.433469\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc_rules/user.py",
    "groupTitle": "User"
  },
  {
    "type": "POST",
    "url": "/api/social/user/login/",
    "title": "Log in",
    "name": "Log_in",
    "group": "User",
    "description": "<p>Log in</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "login",
            "description": "<p>User unique login</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>User password</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "like",
            "description": "<p>Id of got user</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "auth_token",
            "description": "<p>Now it is just test</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"auth_token\": 'test'\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc_rules/user.py",
    "groupTitle": "User"
  },
  {
    "type": "POST",
    "url": "/api/social/user/signup/",
    "title": "Sign up",
    "name": "Sign_up",
    "group": "User",
    "description": "<p>Sign up</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "login",
            "description": "<p>User unique login</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>User password</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "like",
            "description": "<p>Id of created user</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc_rules/user.py",
    "groupTitle": "User"
  }
] });
