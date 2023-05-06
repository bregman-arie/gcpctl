// Copyright 2023 Arie Bregman, Inc.
// All Rights Reserved.
//
//	Licensed under the Apache License, Version 2.0 (the "License"); you may
//	not use this file except in compliance with the License. You may obtain
//	a copy of the License at
//
//	     http://www.apache.org/licenses/LICENSE-2.0
//
//	Unless required by applicable law or agreed to in writing, software
//	distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
//	WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
//	License for the specific language governing permissions and limitations
//	under the License.
package cmd

import (
	"github.com/spf13/cobra"
)

const Version = "0.0.1"
:
var (

	// Root Cobra command - gcpctl
	RootCmd = &cobra.Command{
		Use:     "gcpctl",
		Version: Version,
		Short:   "Google Cloud Platform Alternative CLI",
		PersistentPreRun: func(cob *cobra.Command, args []string) {
		},
	}
)

func init() {
	// Set up logging and anything else
	cobra.OnInitialize(initConfig)
:
	// Set up our flags
	RootCmd.PersistentFlags().BoolVarP(&VerboseFlag, "verbose", "v", false, "enable verbose logging")
	RootCmd.PersistentFlags().BoolVarP(&DebugFlag, "debug", "d", false, "enable debug logging")
}

func Execute() {
	if err := RootCmd.Execute(); err != nil {
		logrus.Fatal(err)
	}
}
