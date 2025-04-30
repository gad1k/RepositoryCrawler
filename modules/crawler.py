from modules.file_diff import FileDiff


class Crawler:
    def __init__(self):
        self.file_diffs = list()


    def inspect_repository(self):
        src = """
        col_01 int not null,
        col_02 varchar(50) not null,
        col_03 varchar(200),
        col_04 varchar(50) not null,
        col_05 varchar(50),
        col_06 int,
        col_07 varchar(1) not null,
        col_08 date not null,
        col_09 datetime2 not null,
        col_10 datetime2 not null
        """

        trg = """
        col_01 int not null,
        col_02 varchar(50) not null,
        col_22 varchar(50) not null,
        col_03 varchar(200),
        col_04 varchar(50) not null,
        col_05 varchar(50),
        col_09 datetime2 not null,
        col_66 int,
        col_07 varchar(2) not null,
        col_08 date not null,
        col_10 datetime2 not null
        """

        file_diff = FileDiff(src, trg)
        file_diff.build_scripts()
        file_diff.render_scripts()
