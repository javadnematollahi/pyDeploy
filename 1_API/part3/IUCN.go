package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://apiv3.iucnredlist.org/api/v3/species/synonym/Felis%20pardus?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "sails.sid=s%3APSCL0kQ0Id6W-sjh3qyvSZElwJoASLrw.snwc7LBRhPW9BKAXxQn0xMbem241bXAAwKjqEAnMza8")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}