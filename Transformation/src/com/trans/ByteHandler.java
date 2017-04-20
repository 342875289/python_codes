package com.trans;

import org.apache.mina.core.buffer.IoBuffer;
import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IoSession;

public class ByteHandler extends IoHandlerAdapter {

	private int count = 0;

	/**
	 * ��һ���ͻ������ӽ���ʱ
	 */
	@Override
	public void sessionOpened(IoSession session) throws Exception {

		System.out.println("incoming client: " + session.getRemoteAddress());

	}

	/**
	 * ��һ���ͻ��˹ر�ʱ
	 */
	@Override
	public void sessionClosed(IoSession session) throws Exception {

		System.out.println(session.getRemoteAddress() + "is Disconnection");

	}

	@Override
	public void messageReceived(IoSession session, Object message) throws Exception {

		IoBuffer ioBuffer = (IoBuffer) message;
		byte[] b = new byte[ioBuffer.limit()];
		ioBuffer.get(b);

		String msg = new String(b);

		System.out.println("�յ��ͻ��˷�������ϢΪ" + "  " + msg);

		// ��������Ϣ���͸��ͻ���
		// session.write(str + count);
	}
}
