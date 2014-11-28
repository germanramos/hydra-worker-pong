package main

import (
	"os"

	worker "github.com/innotech/hydra-worker-pong/vendors/github.com/innotech/hydra-worker-lib"
)

func main() {
	pongWorker, _ := worker.NewWorker(os.Args)
	fn := func(instances []interface{}, clientParams map[string][]string, args map[string]interface{}) []interface{} {
		return instances
	}
	pongWorker.Run(fn)
}
