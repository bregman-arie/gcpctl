package folders

import (
	"context"
	"fmt"

	"google.golang.org/api/cloudresourcemanager/v1"
	"google.golang.org/api/option"
)

func GetFolders() {
	ctx := context.Background()

	// Create a new Cloud Resource Manager client using application default credentials.
	crmService, err := cloudresourcemanager.NewService(ctx, option.WithScopes(cloudresourcemanager.CloudPlatformScope))
	if err != nil {
		fmt.Printf("Failed to create Cloud Resource Manager client: %v\n", err)
		return
	}

	// Call the Cloud Resource Manager API to list the folders.
	folders, err := crmService.Folders.List().Do()
	if err != nil {
		fmt.Printf("Failed to list folders: %v\n", err)
		return
	}

	// Print the folder names.
	fmt.Println("Folders:")
	for _, folder := range folders.Folders {
		fmt.Printf("- %v (%v)\n", folder.DisplayName, folder.Name)
	}
}
