package cmd

import (
	folders "github.com/bregman-arie/gcpctl/pkg/folders"

	"github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
)

var (
	ListCmd = &cobra.Command{
		Use:     "list",
		Aliases: []string{"get"},
		Short:   "Perform various list related actions",
		Run: func(cob *cobra.Command, args []string) {
			if len(args) == 0 {
				cob.Help()
			}
		},
	}

	ListFoldersCmd = &cobra.Command{
		Use:     "folders",
		Aliases: []string{"folders"},
		Short:   "List folders",
		Run: func(cob *cobra.Command, args []string) {
			logrus.Info("Listing folders...")
			folders.GetFolders()
		},
	}

	ListProjectsCmd = &cobra.Command{
		Use:     "projects",
		Aliases: []string{"proj"},
		Short:   "List projects",
		Run: func(cob *cobra.Command, args []string) {
			logrus.Info("Listing Projects...")
		},
	}

	ListGKEClustersCmd = &cobra.Command{
		Use:     "gke-clusters",
		Aliases: []string{"clusters"},
		Short:   "List GKE clusters",
		Run: func(cob *cobra.Command, args []string) {
			logrus.Info("Listing GKE clusters...")
		},
	}

	ListGKENodePoolsCmd = &cobra.Command{
		Use:     "gke-node-pools",
		Aliases: []string{"gnp"},
		Short:   "List GKE node pools",
		Run: func(cob *cobra.Command, args []string) {
			logrus.Info("Listing GKE node pools...")
		},
	}
)

func init() {
	ListCmd.AddCommand(ListFoldersCmd)
	ListCmd.AddCommand(ListProjectsCmd)
	ListCmd.AddCommand(ListGKEClustersCmd)
	ListCmd.AddCommand(ListGKENodePoolsCmd)
	RootCmd.AddCommand(ListCmd)
}
