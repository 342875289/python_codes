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

import java.io.IOException;
import java.net.InetSocketAddress;

import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.core.session.IoSession;
import org.apache.mina.filter.executor.ExecutorFilter;
import org.apache.mina.transport.socket.nio.NioDatagramAcceptor;

public class UdpServer extends IoHandlerAdapter {
	Trans trans;
	public static final int PORT = 9124;
	public static final int MAX_RECEIVED = 100000;

	@Override
	public void exceptionCaught(IoSession session, Throwable cause) throws Exception {
		cause.printStackTrace();
		session.close(true);
		trans.udpsession = null;
	}

	@Override
	public void messageReceived(IoSession session, Object message) throws Exception {
		// System.out.println("------>"+(String)message);
		// session.write(message);
		if (null != trans.serialsession)
			trans.serialsession.write(message);
	}

	@Override
	public void sessionClosed(IoSession session) throws Exception {
//		System.out.println("Session closed...");
		trans.udpsession = null;
	}

	@Override
	public void sessionCreated(IoSession session) throws Exception {
		trans.udpsession = session;
//		System.out.println("Session created...");
	}

	@Override
	public void sessionIdle(IoSession session, IdleStatus status) throws Exception {
//		System.out.println("Session idle...");
	}

	@Override
	public void sessionOpened(IoSession session) throws Exception {
//		System.out.println("Session Opened...");
		trans.udpsession = session;
	}

	public UdpServer(Trans trans) throws IOException {
		this.trans = trans;
		this.trans.udpServer = this;
		NioDatagramAcceptor acceptor = new NioDatagramAcceptor();
		acceptor.setHandler(this);
//	    DefaultIoFilterChainBuilder chain = acceptor.getFilterChain();
//	    chain.addLast("logger", new LoggingFilter());
//		acceptor.getFilterChain().addLast("codec",
//				new ProtocolCodecFilter(new TextLineCodecFactory(Charset.forName("UTF-8"))));
		
		// 设置buffer的长度
		//acceptor.getSessionConfig().setReadBufferSize(2048);
		acceptor.getFilterChain().addLast("threadPool", new ExecutorFilter());
		acceptor.bind(new InetSocketAddress(PORT));	
	}

}
