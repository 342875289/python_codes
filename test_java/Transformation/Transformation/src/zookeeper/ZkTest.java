package zookeeper;

import java.io.IOException;
import java.util.HashMap;
import java.util.concurrent.CountDownLatch;

import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.KeeperException;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.Watcher.Event.KeeperState;
import org.apache.zookeeper.ZooDefs.Ids;
import org.apache.zookeeper.ZooKeeper;

import com.alibaba.fastjson.JSON;

public class ZkTest {

	public static void main(String[] args) throws IOException, InterruptedException, KeeperException {
		final CountDownLatch countDownLatch = new CountDownLatch(1);
		ZooKeeper zk = new ZooKeeper("192.168.6.128:2181,192.168.6.131:2181,192.168.6.132:2181", 20000, new Watcher() {
			@Override
			public void process(WatchedEvent event) {
				if (KeeperState.SyncConnected == event.getState()) {
					countDownLatch.countDown();
				}
			}
		});
		countDownLatch.await();
//		if (null == zk.exists("/preprocess", false)) {
//			zk.create("/preprocess", null, Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT);
//		}
//		if (null == zk.exists("/preprocess/result", false)) {
//			zk.create("/preprocess/result", null, Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT);
//		}
//		if (null == zk.exists("/preprocess/result/123", false)) {
//			zk.create("/preprocess/result/123", null, Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT);
//		}
		HashMap<String, Object> item1 = new HashMap<>();
		item1.put("port", 3333);
		item1.put("ip", "30.14.40.17");
		item1.put("linknum", 3);
		
		HashMap<String, Object> item2 = new HashMap<>();
		item2.put("port", 335);
		item2.put("ip", "30.14.40.18");
		item2.put("linknum", 546);
		
		zk.create("/30.14.40.17", JSON.toJSONString(item1).getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL);
		zk.create("/30.14.40.18", JSON.toJSONString(item2).getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL);
//		
//		zk.create("/30.14.40.17", "3".getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL);
//		zk.create("/30.14.40.18", "45".getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL);
//		zk.create("/30.14.40.19", "7".getBytes(), Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL);
//		//zkstate: CONNECTED连接成功
//		System.out.println("zkstate: "+zk.getState());
//		for (String string : zk.getChildren("/zookeeper", false)) {
//			System.out.println(string);
//			//System.out.println(new String(zk.getData("/preprocess/result/123/" + string, false, null)));
//			System.out.println("==================");
//		}
		
		while (true) {
			Thread.sleep(50000);
			
		}
		
		
		//zk.close();
	}

}
