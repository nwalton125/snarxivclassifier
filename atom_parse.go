package main

import (
	"github.com/mmcdole/gofeed"
	"io/ioutil"
  "strings"
  "fmt"
)

func main() {
	url := "http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1000"
  fp := gofeed.NewParser()
  feed, _ := fp.ParseURL(url)
  var titels []string
	for _, item := range feed.Items {
    cleaned := strings.Replace(item.Title, "\n  ", " ", 100)
    fmt.Println(cleaned)
		titels = append(titels, cleaned)
	}
	ioutil.WriteFile("arxiv.txt", []byte(strings.Join(titels, "\n")), 0644)
}
