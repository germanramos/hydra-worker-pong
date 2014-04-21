package main

import (
	// "encoding/json"
	// "log"
	"os"

	worker "github.com/innotech/hydra-worker-pong/vendors/github.com/innotech/hydra-worker-lib"
)

func main() {
	if len(os.Args) < 3 {
		panic("Invalid number of arguments, you need to add at least the arguments for the server address and the service name")
	}
	serverAddr := os.Args[1]  // e.g. "tcp://localhost:5555"
	serviceName := os.Args[2] // e.g. pong
	verbose := len(os.Args) >= 4 && os.Args[3] == "-v"

	// New Worker connected to Hydra Load Balancer
	pongWorker := worker.NewWorker(serverAddr, serviceName, verbose)
	fn := func(instances []map[string]interface{}, args map[string]string) []interface{} {
		computedInstances := make([]interface{}, 0)
		for _, instance := range instances {
			computedInstances = append(computedInstances, instance["Info"].(map[string]interface{})["uri"].(string))
		}
		return computedInstances
	}
	pongWorker.Run(fn)
}
