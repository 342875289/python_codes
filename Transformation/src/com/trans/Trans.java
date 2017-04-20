package com.trans;

import java.io.IOException;

import org.apache.mina.core.session.IoSession;

public class Trans {
	public  UdpServer udpServer;
	public  SerialServer serialServer;
	public	IoSession udpsession;
	public	IoSession serialsession;
	public static void main(String[] args) throws IOException {
		Trans trans = new Trans();
		UdpServer udpServer = new UdpServer(trans);
		SerialServer serialServer = new SerialServer(trans);
		System.out.println("Server started !");
	}

}
