"""Various dictionaies mapping pretty flags from strace to the values to which
they correspond
"""

OS_CONST = {
    # asm-generic/fcntl.h
    'O_RDONLY': 00000000,
    'O_WRONLY': 00000001,
    'O_APPEND': 00002000,
    'O_RDWR': 00000002,
    'O_LARGEFILE': 00100000,
    'SOL_SOCKET': 1,
    'SO_ERROR': 4,
    # asm-generic/fcntl.h
    'O_NONBLOCK': 0004000,
    'O_NOFOLLOW': 00400000,
    'O_DIRECTORY': 00200000

}

SOCK_CONST = {
    'SOCK_STREAM': 1,
    'SOCK_DGRAM': 2
}

STAT_CONST = {
    'S_IFMT': 00170000,
    'S_IFSOCK': 0140000,
    'S_IFLNK': 0120000,
    'S_IFREG': 0100000,
    'S_IFBLK': 0060000,
    'S_IFDIR': 0040000,
    'S_IFCHR': 0020000,
    'S_IFIFO': 0010000,
    'S_ISUID': 0004000,
    'S_ISGID': 0002000,
    'S_ISVTX': 0001000
}

FCNTL64_CMD_TO_INT = {
    'F_DUPFD':	0,
    'F_GETFD':	1,
    'F_SETFD':	2,
    'F_GETFL':	3,
    'F_SETFL':	4,
    'F_GETLK':	5,
    'F_SETLK':	6,
    'F_SETLKW': 7,
    'F_SETOWN': 8,
    'F_GETOWN': 9,
    'F_SETSIG': 10,
    'F_GETSIG': 11,
    'F_GETLK64': 12,
    'F_SETLK64': 13,
    'F_SETLKW64': 14,
    'F_SETOWN_EX': 15,
    'F_GETOWN_EX': 16,
    'F_GETOWNER_UIDS': 17
}

FCNTL64_INT_TO_CMD = {y: x for x, y in FCNTL64_CMD_TO_INT.iteritems()}

SIGNAL_DFLT_HANDLER_TO_INT = {
    'SIG_DFL': 0,
    'SIG_ERR': -1,
    'SIG_IGN': 1
}

SIGNAL_INT_TO_DFLT_HANDLER = {y: x for x, y
                              in SIGNAL_DFLT_HANDLER_TO_INT.iteritems()}


SIGNAL_FLAG_TO_HEX = {
    'SA_NOCLDSTOP': 0x00000001,
    'SA_NOCLDWAIT': 0x00000002,
    'SA_SIGINFO':   0x00000004,
    'SA_RESTORER':  0x04000000,
    'SA_INTERRUPT': 0x20000000,
    'SA_RESTART':   0x10000000,
    'SA_ONSTACK':   0x08000000,
    'SA_STACK':     0x08000000,  # SA_ONSTACK alias
    'SA_NODEFER':   0x40000000,
    'SA_NOMASK':    0x40000000,  # SA_NODEFER alias
    'SA_RESETHAND': 0x80000000,
    'SA_ONESHOT':   0x80000000   # SA_RESETHAND alias
}

SIGNAL_HEX_TO_FLAG = {y: x for x, y in SIGNAL_FLAG_TO_HEX.iteritems()}

SIGNAL_SIG_TO_INT = {
    'SIGHUP': 1,
    'SIGINT': 2,
    'SIGQUIT': 3,
    'SIGILL': 4,
    'SIGTRAP': 5,
    'SIGABRT': 6,
    'SIGIOT': 6,
    'SIGBUS': 7,
    'SIGFPE': 8,
    'SIGKILL': 9,
    'SIGUSR1': 10,
    'SIGSEGV': 11,
    'SIGUSR2': 12,
    'SIGPIPE': 13,
    'SIGALRM': 14,
    'SIGTERM': 15,
    'SIGSTKFLT': 16,
    'SIGCHLD': 17,
    'SIGCONT': 18,
    'SIGSTOP': 19,
    'SIGTSTP': 20,
    'SIGTTIN': 21,
    'SIGTTOU': 22,
    'SIGURG': 23,
    'SIGXCPU': 24,
    'SIGXFSZ': 25,
    'SIGVTALRM': 26,
    'SIGPROF': 27,
    'SIGWINCH': 28,
    'SIGIO': 29,
    'SIGPOLL': 29,
    'SIGLOST': 29,
    'SIGPWR': 30,
    'SIGSYS': 31,
    'SIGUNUSED': 31,
    'SIGRTMIN': 32
}

SIGNAL_INT_TO_SIG = {y: x for x, y in SIGNAL_SIG_TO_INT.iteritems()}

IOCTLS_IOCTL_TO_INT = {
    'TCGETS': 0x5401,
    'TCSETS': 0x5402,
    'TCSETSW': 0x5403,
    'TCSETSF': 0x5404,
    'TCGETA': 0x5405,
    'TCSETA': 0x5406,
    'TCSETAW': 0x5407,
    'TCSETAF': 0x5408,
    'TCSBRK': 0x5409,
    'TCXONC': 0x540A,
    'TCFLSH': 0x540B,
    'TIOCEXCL':	0x540C,
    'TIOCNXCL':	0x540D,
    'TIOCSCTTY': 0x540E,
    'TIOCGPGRP': 0x540F,
    'TIOCSPGRP': 0x5410,
    'TIOCOUTQ': 0x5411,
    'TIOCSTI': 0x5412,
    'TIOCGWINSZ': 0x5413,
    'TIOCSWINSZ': 0x5414,
    'TIOCMGET':	0x5415,
    'TIOCMBIS':	0x5416,
    'TIOCMBIC':	0x5417,
    'TIOCMSET':	0x5418,
    'TIOCGSOFTCAR': 0x5419,
    'TIOCSSOFTCAR': 0x541A,
    'FIONREAD':	0x541B,
    'TIOCINQ':	0x541B,
    'TIOCLINUX': 0x541C,
    'TIOCCONS':	0x541D,
    'TIOCGSERIAL': 0x541E,
    'TIOCSSERIAL': 0x541F,
    'TIOCPKT': 0x5420,
    'FIONBIO': 0x5421,
    'TIOCNOTTY': 0x5422,
    'TIOCSETD':	0x5423,
    'TIOCGETD':	0x5424,
    'TCSBRKP': 0x5425,
    'TIOCSBRK':	0x5427,
    'TIOCCBRK':	0x5428,
    'TIOCGSID':	0x5429,
    'TIOCGRS485': 0x542E,
    'TIOCSRS485': 0x542F,
    'TCGETX': 0x5432,
    'TCSETX': 0x5433,
    'TCSETXF': 0x5434,
    'TCSETXW': 0x5435,
    'TIOCVHANGUP': 0x5437,
    'FIONCLEX':	0x5450,
    'FIOCLEX': 0x5451,
    'FIOASYNC':	0x5452,
    'TIOCSERCONFIG': 0x5453,
    'TIOCSERGWILD': 0x5454,
    'TIOCSERSWILD': 0x5455,
    'TIOCGLCKTRMIOS': 0x5456,
    'TIOCSLCKTRMIOS': 0x5457,
    'TIOCSERGSTRUCT': 0x5458,
    'TIOCSERGETLSR':   0x5459,
    'TIOCSERGETMULTI': 0x545A,
    'TIOCSERSETMULTI': 0x545B,
    'TIOCMIWAIT': 0x545C,
    'TIOCGICOUNT': 0x545D,
}

IOCTLS_INT_TO_IOCTL = {y: x for x, y in IOCTLS_IOCTL_TO_INT.iteritems()}

SHUTDOWN_INT_TO_CMD = {
    0: 'SHUT_RD',
    1: 'SHUT_WR',
    2: 'SHUT_RDWR'
}

SHUTDOWN_CMD_TO_INT = {y: x for x, y in SHUTDOWN_INT_TO_CMD.iteritems()}

SIGPROCMASK_INT_TO_CMD = {
    0: 'SIG_BLOCK',
    1: 'SIG_UNBLOCK',
    2: 'SIG_SETMASK'
}

SIGPROC_CMD_TO_INT = {y: x for x, y in SIGPROCMASK_INT_TO_CMD.iteritems()}

PERM_INT_TO_PERM = {
    4: 'R_OK',
    2: 'W_OK',
    1: 'X_OK',
    0: 'F_OK'
}

PERM_PERM_TO_INT = {y: x for x, y in PERM_INT_TO_PERM.iteritems()}

PROTOFAM_INT_TO_FAM = {
    0: 'PF_UNSPEC',
    1: 'PF_LOCAL',
    2: 'PF_INET',
    3: 'PF_AX25',
    4: 'PF_IPX',
    5: 'PF_APPLETALK',
    6: 'PF_NETROM',
    7: 'PF_BRIDGE',
    8: 'PF_ATMPVC',
    9: 'PF_X25',
    10: 'PF_INET6',
    11: 'PF_ROSE',
    12: 'PF_DECnet',
    13: 'PF_NETBEUI',
    14: 'PF_SECURITY',
    15: 'PF_KEY',
    16: 'PF_NETLINK',
    17: 'PF_PACKET',
    18: 'PF_ASH',
    19: 'PF_ECONET',
    20: 'PF_ATMSVC',
    21: 'PF_RDS',
    22: 'PF_SNA',
    23: 'PF_IRDA',
    24: 'PF_PPPOX',
    25: 'PF_WANPIPE',
    26: 'PF_LLC',
    29: 'PF_CAN',
    30: 'PF_TIPC',
    31: 'PF_BLUETOOTH',
    32: 'PF_IUCV',
    33: 'PF_RXRPC',
    34: 'PF_ISDN',
    35: 'PF_PHONET',
    36: 'PF_IEEE802154',
    37: 'PF_CAIF',
    38: 'PF_ALG',
    39: 'PF_NFC',
    40: 'PF_VSOCK',
    41: 'PF_MAX',
}

PROTOFAM_FAM_TO_INT = {y: x for x, y in PROTOFAM_INT_TO_FAM.iteritems()}

ADDRFAM_FAM_TO_INT = {
    'AF_UNSPEC': PROTOFAM_FAM_TO_INT['PF_UNSPEC'],
    'AF_LOCAL': PROTOFAM_FAM_TO_INT['PF_LOCAL'],
    'AF_UNIX':  PROTOFAM_FAM_TO_INT['PF_LOCAL'],
    'AF_FILE':  PROTOFAM_FAM_TO_INT['PF_LOCAL'],
    'AF_INET':  PROTOFAM_FAM_TO_INT['PF_INET'],
    'AF_AX25':  PROTOFAM_FAM_TO_INT['PF_AX25'],
    'AF_IPX':  PROTOFAM_FAM_TO_INT['PF_IPX'],
    'AF_APPLETALK': PROTOFAM_FAM_TO_INT['PF_APPLETALK'],
    'AF_NETROM': PROTOFAM_FAM_TO_INT['PF_NETROM'],
    'AF_BRIDGE': PROTOFAM_FAM_TO_INT['PF_BRIDGE'],
    'AF_ATMPVC': PROTOFAM_FAM_TO_INT['PF_ATMPVC'],
    'AF_X25':  PROTOFAM_FAM_TO_INT['PF_X25'],
    'AF_INET6': PROTOFAM_FAM_TO_INT['PF_INET6'],
    'AF_ROSE':  PROTOFAM_FAM_TO_INT['PF_ROSE'],
    'AF_DECnet': PROTOFAM_FAM_TO_INT['PF_DECnet'],
    'AF_NETBEUI': PROTOFAM_FAM_TO_INT['PF_NETBEUI'],
    'AF_SECURITY': PROTOFAM_FAM_TO_INT['PF_SECURITY'],
    'AF_KEY':  PROTOFAM_FAM_TO_INT['PF_KEY'],
    'AF_NETLINK': PROTOFAM_FAM_TO_INT['PF_NETLINK'],
    'AF_ROUTE': PROTOFAM_FAM_TO_INT['PF_NETLINK'],
    'AF_PACKET': PROTOFAM_FAM_TO_INT['PF_PACKET'],
    'AF_ASH':  PROTOFAM_FAM_TO_INT['PF_ASH'],
    'AF_ECONET': PROTOFAM_FAM_TO_INT['PF_ECONET'],
    'AF_ATMSVC': PROTOFAM_FAM_TO_INT['PF_ATMSVC'],
    'AF_RDS':  PROTOFAM_FAM_TO_INT['PF_RDS'],
    'AF_SNA':  PROTOFAM_FAM_TO_INT['PF_SNA'],
    'AF_IRDA':  PROTOFAM_FAM_TO_INT['PF_IRDA'],
    'AF_PPPOX': PROTOFAM_FAM_TO_INT['PF_PPPOX'],
    'AF_WANPIPE': PROTOFAM_FAM_TO_INT['PF_WANPIPE'],
    'AF_LLC':  PROTOFAM_FAM_TO_INT['PF_LLC'],
    'AF_CAN':  PROTOFAM_FAM_TO_INT['PF_CAN'],
    'AF_TIPC':  PROTOFAM_FAM_TO_INT['PF_TIPC'],
    'AF_BLUETOOTH': PROTOFAM_FAM_TO_INT['PF_BLUETOOTH'],
    'AF_IUCV':  PROTOFAM_FAM_TO_INT['PF_IUCV'],
    'AF_RXRPC': PROTOFAM_FAM_TO_INT['PF_RXRPC'],
    'AF_ISDN':  PROTOFAM_FAM_TO_INT['PF_ISDN'],
    'AF_PHONET': PROTOFAM_FAM_TO_INT['PF_PHONET'],
    'AF_IEEE802154': PROTOFAM_FAM_TO_INT['PF_IEEE802154'],
    'AF_CAIF':  PROTOFAM_FAM_TO_INT['PF_CAIF'],
    'AF_ALG':  PROTOFAM_FAM_TO_INT['PF_ALG'],
    'AF_NFC':  PROTOFAM_FAM_TO_INT['PF_NFC'],
    'AF_VSOCK': PROTOFAM_FAM_TO_INT['PF_VSOCK'],
    'AF_MAX':  PROTOFAM_FAM_TO_INT['PF_MAX']
}

ADDRFAM_INT_TO_FAM = {y: x for x, y in ADDRFAM_FAM_TO_INT.iteritems()}

SOCKTYPE_INT_TO_TYPE = {
    1: 'SOCK_STREAM',
    2: 'SOCK_DGRAM',
    3: 'SOCK_RAW',
    4: 'SOCK_DRM',
    5: 'SOCK_SEQPACKET',
    6: 'SOCK_DCCP',
    10: 'SOCK_PACKET'
}

SOCKTYPE_TYPE_TO_INT = {y: x for x, y in SOCKTYPE_INT_TO_TYPE.iteritems()}

STACK_INT_TO_SS = {
    1: 'SS_ONSTACK',
    2: 'SS_DISABLE'
}

STACK_SS_TO_INT = {y: x for x, y in STACK_INT_TO_SS.iteritems()}

POLL_INT_TO_EVENT = {
    0x001: 'POLLIN',
    0x002: 'POLLPRI',
    0x004: 'POLLOUT',
    0x400: 'POLLMSG',
    0x1000: 'POLLREMOVE',
    0x2000: 'POLLRDHUP',
    0x008: 'POLLERR',
    0x010: 'POLLHUP',
    0x020: 'POLLNVAL',
}

POLL_EVENT_TO_INT = {y: x for x, y in POLL_INT_TO_EVENT.iteritems()}


MAGIC_NAME_TO_MAGIC = {
    'ADFS_SUPER_MAGIC': 0xadf5,
    'AFFS_SUPER_MAGIC': 0xadff,
    'AFS_SUPER_MAGIC': 0x5346414F,
    'AUTOFS_SUPER_MAGIC': 0x0187,
    'CODA_SUPER_MAGIC': 0x73757245,
    'CRAMFS_MAGIC': 0x28cd3d45,
    'CRAMFS_MAGIC_WEND': 0x453dcd28,
    'DEBUGFS_MAGIC': 0x64626720,
    'SECURITYFS_MAGIC': 0x73636673,
    'SELINUX_MAGIC': 0xf97cff8c,
    'SMACK_MAGIC': 0x43415d53,
    'RAMFS_MAGIC': 0x858458f6,
    'TMPFS_MAGIC': 0x01021994,
    'HUGETLBFS_MAGIC': 0x958458f6,
    'SQUASHFS_MAGIC': 0x73717368,
    'ECRYPTFS_SUPER_MAGIC': 0xf15f,
    'EFS_SUPER_MAGIC': 0x414A53,
    'EXT2_SUPER_MAGIC': 0xEF53,
    'EXT3_SUPER_MAGIC': 0xEF53,
    'XENFS_SUPER_MAGIC': 0xabba1974,
    'EXT4_SUPER_MAGIC': 0xEF53,
    'BTRFS_SUPER_MAGIC': 0x9123683E,
    'NILFS_SUPER_MAGIC': 0x3434,
    'F2FS_SUPER_MAGIC': 0xF2F52010,
    'HPFS_SUPER_MAGIC': 0xf995e849,
    'ISOFS_SUPER_MAGIC': 0x9660,
    'PSTOREFS_MAGIC': 0x6165676C,
    'EFIVARFS_MAGIC': 0xde5e81e4,
    'HOSTFS_SUPER_MAGIC': 0x00c0ffee,
    'MINIX_SUPER_MAGIC': 0x137F,
    'MINIX_SUPER_MAGIC2': 0x138F,
    'MINIX2_SUPER_MAGIC': 0x2468,
    'MINIX2_SUPER_MAGIC2': 0x2478,
    'MINIX3_SUPER_MAGIC': 0x4d5a,
    'MSDOS_SUPER_MAGIC': 0x4d44,
    'NCP_SUPER_MAGIC': 0x564c,
    'NFS_SUPER_MAGIC': 0x6969,
    'OPENPROM_SUPER_MAGIC': 0x9fa1,
    'QNX4_SUPER_MAGIC': 0x002f,
    'QNX6_SUPER_MAGIC': 0x68191122,
    'REISERFS_SUPER_MAGIC': 0x52654973,
    'SMB_SUPER_MAGIC': 0x517B,
    'CGROUP_SUPER_MAGIC': 0x27e0eb,
    'STACK_END_MAGIC': 0x57AC6E9D,
    'V9FS_MAGIC': 0x01021997,
    'BDEVFS_MAGIC': 0x62646576,
    'BINFMTFS_MAGIC': 0x42494e4d,
    'DEVPTS_SUPER_MAGIC': 0x1cd1,
    'FUTEXFS_SUPER_MAGIC': 0xBAD1DEA,
    'PIPEFS_MAGIC': 0x50495045,
    'PROC_SUPER_MAGIC': 0x9fa0,
    'SOCKFS_MAGIC': 0x534F434B,
    'SYSFS_MAGIC': 0x62656572,
    'USBDEVICE_SUPER_MAGIC': 0x9fa2,
    'MTD_INODE_FS_MAGIC': 0x11307854,
    'ANON_INODE_FS_MAGIC': 0x09041934,
    'BTRFS_TEST_MAGIC': 0x73727279,
    'NSFS_MAGIC': 0x6e736673,
}

MAGIC_MAGIC_TO_NAME = {y: x for x, y in MAGIC_NAME_TO_MAGIC.iteritems()}


EPOLL_EVENT_TO_NUM = {
    'EPOLLIN': 0x001,
    'EPOLLPRI': 0x002,
    'EPOLLOUT': 0x004,
    'EPOLLRDNORM': 0x040,
    'EPOLLRDBAND': 0x080,
    'EPOLLWRNORM': 0x100,
    'EPOLLWRBAND': 0x200,
    'EPOLLMSG': 0x400,
    'EPOLLERR': 0x008,
    'EPOLLHUP': 0x010,
    'EPOLLRDHUP': 0x2000,
    # Be careful of these below
    'EPOLLWAKEUP': 2000000,
    'EPOLLONESHOT': 40000000,
    'EPOLLET': 80000000
}


EPOLL_NUM_TO_EVENT = {y: x for x, y in EPOLL_EVENT_TO_NUM.iteritems()}
