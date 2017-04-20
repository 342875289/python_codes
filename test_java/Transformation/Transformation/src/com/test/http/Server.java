package com.test.http;

import java.net.InetSocketAddress;
import org.apache.mina.filter.codec.ProtocolCodecFilter;
import org.apache.mina.filter.logging.LoggingFilter;
import org.apache.mina.transport.socket.nio.NioSocketAcceptor;
public class Server {
    private static int DEFAULT_PORT = 8080;
    public static void main(String[] args) {
        int port = DEFAULT_PORT;
        for (int i = 0; i < args.length; i++) {
            if (args[i].equals("-port")) {
                port = Integer.parseInt(args[i + 1]);
            }
        }
        try {
        	NioSocketAcceptor acceptor = new NioSocketAcceptor();
        	acceptor.getFilterChain().addLast(
                    "protocolFilter",
                    new ProtocolCodecFilter(
                            new HttpServerProtocolCodecFactory()));
        	acceptor.getFilterChain().addLast("logger", new LoggingFilter());
            acceptor.setHandler(new ServerHandler());
            acceptor
                    .bind(new InetSocketAddress(port));
            System.out.println("Server now listening on port " + port);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
