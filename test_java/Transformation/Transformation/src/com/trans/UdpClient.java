/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 */
package com.trans;

import java.net.InetSocketAddress;

import org.apache.mina.core.buffer.IoBuffer;
import org.apache.mina.core.future.ConnectFuture;
import org.apache.mina.core.service.IoConnector;
import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IoSession;
import org.apache.mina.transport.socket.nio.NioDatagramConnector;

import util.CommonUtil;

public class UdpClient extends IoHandlerAdapter {

	private IoConnector connector;
	private IoSession session;

	public UdpClient() {
		connector = new NioDatagramConnector();
		connector.setHandler(this);
		// connector.getFilterChain().addLast( "codec", new ProtocolCodecFilter(
		// new TextLineCodecFactory( Charset.forName( "UTF-8" ))));
		ConnectFuture connFuture = connector.connect(new InetSocketAddress("localhost", UdpServer.PORT));
		connFuture.awaitUninterruptibly();
		session = connFuture.getSession();

	}

	@Override
	public void exceptionCaught(IoSession session, Throwable cause) throws Exception {
		cause.printStackTrace();
	}

	@Override
	public void messageReceived(IoSession session, Object message) throws Exception {
		if (!(message instanceof IoBuffer)) {
			return;
		}
		IoBuffer ioBuffer = (IoBuffer) message;
		byte[] readByte = new byte[ioBuffer.limit()];
		ioBuffer.get(readByte);
		System.out.println(CommonUtil.bytesToHexString(readByte));

	}

	public static void main(String[] args) throws Exception {
		UdpClient client = new UdpClient();
		String str = "221";
		byte[] data = str.getBytes();
		IoBuffer buffer = IoBuffer.allocate(data.length);
		buffer.put(data);
		buffer.flip();
		client.session.write(buffer);
		//Thread.sleep(10000);
	//	client.connector.dispose(false);
	}
}
