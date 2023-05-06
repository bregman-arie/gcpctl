package folders

import (
	"context"
	"fmt"
	"log"

	cloudresourcemanager "google.golang.org/api/cloudresourcemanager/v3"
)

func GetFolders() {
	ctx := context.Background()
	svc, err := cloudresourcemanager.NewService(ctx)
	if err != nil {
		log.Fatal(err)
	}
	foldersService := cloudresourcemanager.NewFoldersService(svc)
	foldersListCall := foldersService.List()
	resp, err := foldersListCall.Do()
	if err != nil {
		log.Fatal(err)
	}
	for _, fld := range resp.Folders {
		fmt.Println(fld.DisplayName)
	}
}
