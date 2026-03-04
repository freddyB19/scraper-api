LOL_CHAMPIONS = """
	query QueryLol($count: Int=3) {
	  lol {
	    champions(first: $count) {
	      edges {
	        cursor
	        node {
	          images
	          name
	          url
	        }
	      }
	      pageInfo {
	        hasNextPage
	        hasPreviousPage
	      }
	    }
	  }
	}
"""

LOL_NEWS = """
	query QueryLol($count: Int=3){
	  lol {
	    news(first: $count) {
	      edges {
	        cursor
	        node {
	          category
	          date
	          detail
	          title
	          url
	        }
	      }
	      pageInfo {
	        hasNextPage
	        hasPreviousPage
	      }
	    }
	  }
	}
"""

LOL_NOTES = """
	query QueryLol($count: Int=3){
	  lol {
	    notes(first: $count) {
	      edges {
	        cursor
	        node {
	          category
	          date
	          detail
	          title
	          url
	        }
	      }
	      pageInfo {
	        hasNextPage
	        hasPreviousPage
	      }
	    }
	  }
}
"""

IRACING_CARS = """
query MyQuery($count: Int=3) {
  iracing {
    cars(first: $count) {
      edges {
        cursor
        node {
          image
          isNew
          type
          url
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

IRACING_TRACKS = """
query MyQuery($count: Int=3) {
  iracing {
    tracks(first: $count) {
      edges {
        cursor
        node {
          image
          included
          isNew
          track
          url
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

IRACING_SERIES = """
query MyQuery($count: Int=3) {
  iracing {
    series(first: $count) {
      edges {
        node {
          name
          type {
            image
            name
            url
          }
        }
        cursor
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

IRACING_SEASONS = """
query MyQuery($count: Int=3) {
  iracing {
    seasons(first: $count) {
      edges {
        cursor
        node {
          image
          isLatest
          season
          seasonDate
          seasonUrl
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

IRACING_NEWS = """
query MyQuery($count: Int=3) {
  iracing {
    news(first: $count) {
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
      edges {
        cursor
        node {
          author {
            name
            url
          }
          date
          detail
          image
          title
          url
        }
      }
    }
  }
}
"""


EASPORT_FREE = """
query MyQuery($count: Int=3) {
  easport {
    free(first: $count) {
      edges {
        cursor
        node {
          image
          logo
          title
          url
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

EASPORT_NEWS = """
query MyQuery($count: Int=3) {
  easport {
    news(first: $count) {
      edges {
        cursor
        node {
          date
          detail
          image
          tag
          title
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

EASPORT_NOVELTIES = """
query MyQuery($count: Int=3) {
  easport {
    novelties(first: $count) {
      edges {
        cursor
        node {
          image
          logo
          title
          url
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

EASPORT_SOON = """
query MyQuery($count: Int=3) {
  easport {
    soon(first: $count) {
      edges {
        cursor
        node {
          console {
            type
            url
          }
          date
          genre {
            type
            url
          }
          title
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

EASPORT_UPDATES = """
query MyQuery($count: Int=3) {
  easport {
    updates(first: $count) {
      edges {
        cursor
        node {
          date
          detail
          image
          info
          title
          url
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

MARCA_GAMES = """
query MyQuery($count: Int=3) {
  marca {
    games(first: $count) {
      edges {
        cursor
        node {
          url
          meta
          author
          title
          image
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

LANACION_GAMES = """
query MyQuery($count: Int=3) {
  lanacion {
    games(first: $count) {
      edges {
        cursor
        node {
          url
          date
          image
          title
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

LANACION_TEC = """
query MyQuery($count: Int=3) {
  lanacion {
    tecnology(first: $count) {
      edges {
        cursor
        node {
          url
          date
          image
          title
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

WIRED_ROBOTS = """
query MyQuery($count: Int=3) {
  wired {
    robots(first: $count) {
      edges {
        cursor
        node {
          url
          title
          image
          detail
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

WIRED_BIO = """
query MyQuery($count: Int=3) {
  wired {
    biotechnology(first: $count) {
      edges {
        cursor
        node {
          url
          title
          image
          detail
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

WIRED_NEURO = """
query MyQuery($count: Int=3) {
  wired {
    neuroscience(first: $count) {
      edges {
        cursor
        node {
          url
          title
          image
          detail
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""

WIRED_SPACE = """
query MyQuery($count: Int=3) {
  wired {
    space(first: $count) {
      edges {
        cursor
        node {
          url
          title
          image
          detail
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
      }
    }
  }
}
"""