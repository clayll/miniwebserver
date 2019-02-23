import redis
import rediscluster

if __name__ == '__main__':
    try:
        startup_nodes = [
            {'host': '192.168.81.131', 'port': '7000'},
            {'host': '192.168.81.133', 'port': '7003'},
            {'host': '192.168.81.131', 'port': '7001'},
        ]
        sr = rediscluster.StrictRedisCluster(startup_nodes = startup_nodes,max_connections_per_node=True)
        reuslt = sr.get('age')
        print(reuslt)
    except Exception as e:
        print(e)