package util;

import java.io.File;
import java.io.IOException;

public class CommonUtil {
	public static long count = 1;
	public static void main(String[] args) {
//		System.out.println("Input your folder path：");
//		System.out.println(args==null);
//		System.out.println(getConsoleInputPram()[0].length());
		// <修改文件名>
		 File file = new File("C:/DOCS/a");
		 changeFileName(file);
		 System.out.println(count-1);
		// </修改文件名>
		
		// <清空>
		// SolrOper solrOper = new SolrOper();
		// long start=System.currentTimeMillis();
		// System.out.println("status :"+solrOper.delete("*:*"));
		// long end=System.currentTimeMillis();
		// System.out.println("useTime:"+(end-start));
		// </清空>
	}

	/**
	 * 获取控制台输入的参数数组
	 * @return
	 */
	public static String[] getConsoleInputPram() {
		byte[] b = new byte[1024];
		String[] result={""};
		try {
			int n = System.in.read(b);
			result = new String(b, 0, n).trim().split(" ");
		} catch (IOException e) {
			e.printStackTrace();
		}
		return result;
	}
	 public static String bytesToHexString(byte[] src){       
         StringBuilder stringBuilder = new StringBuilder();       
         if (src == null || src.length <= 0) {       
             return null;       
         }       
         for (int i = 0; i < src.length; i++) {       
             int v = src[i] & 0xFF;       
             String hv = Integer.toHexString(v);       
             if (hv.length() < 2) {       
                 stringBuilder.append(0);       
             }       
             stringBuilder.append(hv);       
         }       
         return stringBuilder.toString();       
     }
	/**
	 * 批量修改指定文件夹下的文件名为数字编号
	 * @param folderPath
	 */
	public static void changeFileName(File folderPath) {
		for (File f : folderPath.listFiles()) {
			if (f.isDirectory()) {
				changeFileName(f);
			} else if (f.isFile()) {
				String filename = f.getName();
				String prefix = filename.substring(filename.lastIndexOf("."));
				f.renameTo(new File(f.getParent() + "\\" + count++ + prefix));

			}
		}
	}

}
