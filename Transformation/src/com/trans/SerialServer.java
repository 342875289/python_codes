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

import org.apache.mina.core.future.ConnectFuture;
import org.apache.mina.core.service.IoConnector;
import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.core.session.IoSession;
import org.apache.mina.transport.serial.SerialAddress;
import org.apache.mina.transport.serial.SerialAddress.DataBits;
import org.apache.mina.transport.serial.SerialAddress.FlowControl;
import org.apache.mina.transport.serial.SerialAddress.Parity;
import org.apache.mina.transport.serial.SerialAddress.StopBits;
import org.apache.mina.transport.serial.SerialConnector;

public class SerialServer extends IoHandlerAdapter {
	Trans trans;
	private static final String PortName = "COM4"; // ´®¿ÚºÅ
	private static final int RATE = 256000; // ²¨ÌØÂÊ
	SerialAddress portAddress;
	/** The connector */
	private IoConnector connector;

	/** The session */
	private IoSession session;

	public SerialServer(Trans trans) {
		this.trans = trans;
		this.trans.serialServer = this;
		connector = new SerialConnector();
		connector.setHandler(this);
		portAddress = new SerialAddress(PortName, RATE, DataBits.DATABITS_8, StopBits.BITS_1, Parity.NONE,
				FlowControl.NONE);
//		connector.getFilterChain().addLast("codec",
//				new ProtocolCodecFilter(new TextLineCodecFactory(Charset.forName("UTF-8"))));
		ConnectFuture connFuture = connector.connect(portAddress);
		connFuture.awaitUninterruptibly();
		session = connFuture.getSession();

	}

	@Override
	public void exceptionCaught(IoSession session, Throwable cause) throws Exception {
		cause.printStackTrace();
		session.close(true);
		trans.serialsession = null;
	}

	@Override
	public void messageReceived(IoSession session, Object message) throws Exception {
		// System.out.println("<------" + (String) message);
		if (null != trans.udpsession)
			trans.udpsession.write(message);
	}

	@Override
	public void messageSent(IoSession session, Object message) throws Exception {
	}

	@Override
	public void sessionClosed(IoSession session) throws Exception {
		trans.serialsession = null;
	}

	@Override
	public void sessionCreated(IoSession session) throws Exception {
		trans.serialsession = session;
	}

	@Override
	public void sessionIdle(IoSession session, IdleStatus status) throws Exception {
	}

	@Override
	public void sessionOpened(IoSession session) throws Exception {
		trans.serialsession = session;
	}

	public static void main(String[] args) throws Exception {
		// SerialServer client = new SerialServer();
		//
		// for (int i = 0; i < 10; i++) {
		// Thread.sleep(2000);
		// String str = Integer.toString(i);
		// session.write(str);
		// System.out.println("---->" + str);
		// }
		//
		// client.connector.dispose(true);
	}
}
