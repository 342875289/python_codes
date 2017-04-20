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
package test;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;

import org.apache.mina.core.buffer.IoBuffer;
import org.apache.mina.core.filterchain.DefaultIoFilterChainBuilder;
import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IoSession;
import org.apache.mina.filter.codec.ProtocolCodecFilter;
import org.apache.mina.filter.codec.textline.TextLineCodecFactory;
import org.apache.mina.filter.executor.ExecutorFilter;
import org.apache.mina.filter.logging.LoggingFilter;
import org.apache.mina.transport.socket.nio.NioDatagramAcceptor;

import util.CommonUtil;

public class UdpServer extends IoHandlerAdapter {

	public static final int PORT = 9124;
	public static final int MAX_RECEIVED = 100000;

	@Override
	public void exceptionCaught(IoSession session, Throwable cause) throws Exception {
		cause.printStackTrace();
		session.close(true);
	}

	@Override
	public void messageReceived(IoSession session, Object message) throws Exception {
		if (!(message instanceof IoBuffer)) {
			return ;
		}
		IoBuffer ioBuffer = (IoBuffer) message;
		//ioBuffer.flip();
		byte[] readByte = new byte[ioBuffer.limit()];
		try {
			ioBuffer.get(readByte);
		} catch (Exception e) {
			System.out.println(e.toString());
		}
	}
/*
	public static byte[] ioBufferToByte(Object message) {
		if (!(message instanceof IoBuffer)) {
			return null;
		}
		IoBuffer ioBuffer = (IoBuffer) message;
		ioBuffer.flip();
		byte[] readByte = new byte[ioBuffer.limit()];
		try {
			ioBuffer.get(readByte);
		} catch (Exception e) {
			System.out.println(e.toString());
		}
		return readByte;
	}
*/
	public UdpServer() throws IOException {
		NioDatagramAcceptor acceptor = new NioDatagramAcceptor();
		acceptor.setHandler(this);
		DefaultIoFilterChainBuilder chain = acceptor.getFilterChain();
//		chain.addLast("logger", new LoggingFilter());
//		acceptor.getFilterChain().addLast("codec",
//				new ProtocolCodecFilter(new TextLineCodecFactory(Charset.forName("UTF-8"))));
		acceptor.getFilterChain().addLast("threadPool", new ExecutorFilter());
		acceptor.bind(new InetSocketAddress(PORT));
		// acceptor.getSessionConfig().setReceiveBufferSize(1024);
		// acceptor.getSessionConfig().setReadBufferSize(1024);
		// acceptor.getSessionConfig().setMaxReadBufferSize(4096);
		System.out.println("Server started...");
	}

	public static void main(String[] args) throws IOException {
		new UdpServer();

	}
}
