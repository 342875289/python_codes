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
package mina.tcp.perf;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.Charset;
import java.util.concurrent.atomic.AtomicInteger;

import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.core.session.IoSession;
import org.apache.mina.filter.codec.ProtocolCodecFilter;
import org.apache.mina.filter.codec.textline.TextLineCodecFactory;
import org.apache.mina.transport.socket.nio.NioSocketAcceptor;

public class TcpServer extends IoHandlerAdapter {
    public static final int PORT = 18567;
    public static final int MAX_RECEIVED = 100000;
    private static long t0;
    private AtomicInteger nbReceived = new AtomicInteger(0);

    @Override
    public void exceptionCaught(IoSession session, Throwable cause) throws Exception {
       // cause.printStackTrace();
        session.close(true);
    }

    @Override
    public void messageReceived(IoSession session, Object message) throws Exception {
        int nb = nbReceived.incrementAndGet();
        if (nb == 1) {
            t0 = System.currentTimeMillis();
        }
        if (nb == MAX_RECEIVED) {
            long t1 = System.currentTimeMillis();
            System.out.println("-------------> end " + (t1 - t0));
        }
        if (nb % 10000 == 0) {
            System.out.println("Received " + nb + " messages");
        }
        session.write(message);
    }

    @Override
    public void sessionClosed(IoSession session) throws Exception {
        System.out.println("Session closed...");
        System.out.println("Nb message received : " + nbReceived.get());
        nbReceived.set(0);
    }

    @Override
    public void sessionCreated(IoSession session) throws Exception {
        System.out.println("Session created...");
    }

    @Override
    public void sessionIdle(IoSession session, IdleStatus status) throws Exception {
        System.out.println("Session idle...");
    }

    @Override
    public void sessionOpened(IoSession session) throws Exception {
        System.out.println("Session Opened...");
        session.write("abc def a d e d a a a b c");
    }

    public TcpServer() throws IOException {
        NioSocketAcceptor acceptor = new NioSocketAcceptor();
        acceptor.setHandler(this);
        acceptor.getFilterChain().addLast("codec",
				new ProtocolCodecFilter(new TextLineCodecFactory(Charset.forName("UTF-8"))));
		
        // The logger, if needed. Commented atm
        //DefaultIoFilterChainBuilder chain = acceptor.getFilterChain();
        //chain.addLast("logger", new LoggingFilter());
        acceptor.bind(new InetSocketAddress(PORT));
        System.out.println("Server started...");
    }

    public static void main(String[] args) throws IOException {
        new TcpServer();
    }
}
