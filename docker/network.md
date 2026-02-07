## 创建集群环境、创建网络环境
- docker swarm init
- docker network create -d overlay --attachable swarm-overlay-network
- docker pull busynet
- docker service create -td --name busybox-global --mode global --network swarm-overlay-network busybox
- docker service rm busybox-global






