anaVersion="DiJet_20140802_MN2010_V16TFPart"
anaType="DiJet"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
#cbWMS="https://wms-cms-analysis.grid.cnaf.infn.it:7443/glite_wms_wmproxy_server"
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
#diObjectType="vector<CompositePtrCandidateT1T2MEt<pat::Muon,pat::Tau> >"
#skimEfficiencyMethod="getSkimEffFromME"
skimEfficiencyMethod="getSkimEff"

#from DiJetAnalysis.DiJetAna.ana.DiJetBalanceSelector import DiJetBalanceSelector
#MySelector  = DiJetBalanceSelector()
#from DiJetAnalysis.DiJetAna.ana.DiJetBalanceVariables import DiJetBalanceVariables
#MyVariables = DiJetBalanceVariables()
#MyVariables.doBalanceAnalisys()
#MySelector.doBalanceAnalysis()

#MyVariables.doDiJetAnalysis()
#MySelector.doDiJetAnalysis()

#MyVariables.doMCResAnalysis()
#MySelector.doMCResAnalysis()



MyVariablesAllEvents="DiJetAnalysis.DiJetAna.ana.BaseVariables"

rootPath="/scratch/scratch0/tfruboes/DATA_dijet/DiJet_20140802_MN2010_V16TFPart/"
sam = {}

sam["Jet-Run2010B-Apr21ReReco-v1"]={}
sam["Jet-Run2010B-Apr21ReReco-v1"]["sgeJobs"]=50
sam["Jet-Run2010B-Apr21ReReco-v1"]["crabJobs"]=470
sam["Jet-Run2010B-Apr21ReReco-v1"]["GT"]='GR_R_42_V19::All'
sam["Jet-Run2010B-Apr21ReReco-v1"]["name"]='Jet-Run2010B-Apr21ReReco-v1'
sam["Jet-Run2010B-Apr21ReReco-v1"]["isData"]=True
sam["Jet-Run2010B-Apr21ReReco-v1"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["Jet-Run2010B-Apr21ReReco-v1"]["numEvents"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1"]["lumiJet15"]=0.0033470000000000001
sam["Jet-Run2010B-Apr21ReReco-v1"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/Jet/DiJet_20140802_MN2010_V16TFPart_Jet-Run2010B-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc//'
sam["Jet-Run2010B-Apr21ReReco-v1"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["Jet-Run2010B-Apr21ReReco-v1"]["lumiDiJet15FB"]='crashMe'
sam["Jet-Run2010B-Apr21ReReco-v1"]["XS"]=-1
sam["Jet-Run2010B-Apr21ReReco-v1"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/Jet/DiJet_20140802_MN2010_V16TFPart_Jet-Run2010B-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc//'
sam["Jet-Run2010B-Apr21ReReco-v1"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/Jet/DiJet_20140802_MN2010_V16TFPart_Jet-Run2010B-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc/'
sam["Jet-Run2010B-Apr21ReReco-v1"]["DS"]='/Jet/Run2010B-Apr21ReReco-v1/AOD'

sam["JetMET-Run2010A-Apr21ReReco-v1"]={}
sam["JetMET-Run2010A-Apr21ReReco-v1"]["sgeJobs"]=50
sam["JetMET-Run2010A-Apr21ReReco-v1"]["crabJobs"]=470
sam["JetMET-Run2010A-Apr21ReReco-v1"]["GT"]='GR_R_42_V19::All'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["name"]='JetMET-Run2010A-Apr21ReReco-v1'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["isData"]=True
sam["JetMET-Run2010A-Apr21ReReco-v1"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["numEvents"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1"]["lumiJet15"]=0.0095250000000000005
sam["JetMET-Run2010A-Apr21ReReco-v1"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMET/DiJet_20140802_MN2010_V16TFPart_JetMET-Run2010A-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc//'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["lumiDiJet15FB"]=2.8380000000000001
sam["JetMET-Run2010A-Apr21ReReco-v1"]["XS"]=-1
sam["JetMET-Run2010A-Apr21ReReco-v1"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMET/DiJet_20140802_MN2010_V16TFPart_JetMET-Run2010A-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc//'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMET/DiJet_20140802_MN2010_V16TFPart_JetMET-Run2010A-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc/'
sam["JetMET-Run2010A-Apr21ReReco-v1"]["DS"]='/JetMET/Run2010A-Apr21ReReco-v1/AOD'

sam["JetMETTau-Run2010A-Apr21ReReco-v1"]={}
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["sgeJobs"]=50
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["crabJobs"]=470
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["GT"]='GR_R_42_V19::All'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["name"]='JetMETTau-Run2010A-Apr21ReReco-v1'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["isData"]=True
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "invtrgWeightJet15RawTF2", RooArgList(v["invtrgWeightJet15RawTF2"]["RooVar"]))'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["numEvents"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["lumiJet15"]=0.013781
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/JetMETTau/DiJet_20140802_MN2010_V16TFPart_JetMETTau-Run2010A-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["json"]='MNTriggerStudies/MNTriggerAna/lumi/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["lumiDiJet15FB"]=0.28277400000000003
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["XS"]=-1
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/JetMETTau/DiJet_20140802_MN2010_V16TFPart_JetMETTau-Run2010A-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc//'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/JetMETTau/DiJet_20140802_MN2010_V16TFPart_JetMETTau-Run2010A-Apr21ReReco-v1/1a444e1fdc949d51e10339e7fb01e1dc/'
sam["JetMETTau-Run2010A-Apr21ReReco-v1"]["DS"]='/JetMETTau/Run2010A-Apr21ReReco-v1/AOD'

sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]={}
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["sgeJobs"]=80
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["crabJobs"]=470
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["GT"]='START42_V16::All'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["weightJet15"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4*trgWeightJet15RawTF2*trgWeightJet15L1RawTF2", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"],v["trgWeightJet15RawTF2"]["RooVar"],v["trgWeightJet15L1RawTF2"]["RooVar"]))'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["name"]='QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["isData"]=False
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["weightPuOnly"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["weightJet15Inverse"]='RooFormulaVar("weight","weight", "generatorWeight*puWeightJet15V4", RooArgList(v["generatorWeight"]["RooVar"],v["puWeightJet15V4"]["RooVar"]))'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["numEvents"]=-1
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["lumiJet15"]='crashMeMC'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["weightNoPu"]='RooFormulaVar("weight","weight", "generatorWeight", RooArgList(v["generatorWeight"]["RooVar"]))'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["json"]=''
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["lumiDiJet15FB"]='crashMeMC'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["pathTrees"]='/XXXTMFTTree/store/user/fruboes/QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/DiJet_20140802_MN2010_V16TFPart_QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/af6a5e4794c9a7da8badc7cf9ea0535b//'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["XS"]=22130000000.0
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["pathPAT"]='/XXXTMFPAT/store/user/fruboes/QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/DiJet_20140802_MN2010_V16TFPart_QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/af6a5e4794c9a7da8badc7cf9ea0535b//'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/fruboes/QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/DiJet_20140802_MN2010_V16TFPart_QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/af6a5e4794c9a7da8badc7cf9ea0535b/'
sam["QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6"]["DS"]='/QCD_Pt-15to3000_TuneZ2star_Flat_HFshowerLibrary_7TeV_pythia6/Summer12-LowPU2010_DR42_PU_S0_START42_V17B-v1/AODSIM'

def icm(sam):
    import socket
    import os
    host = socket.gethostname()
    if ".icm." not in host:
       return sam
    root = "/mnt/lustre/permanent/plgtfruboes/data/"
    thisAna = root + anaVersion + "/"
    for s in sam:
        pathList = set()
        for r,d,f in os.walk(thisAna):
            for files in f:
                if files.endswith(".root"):
                     if s in r:
                        pathList.add( r )
        if len(pathList) != 1:
            print "Problem with paths:", s, pathList
        else:
            sam[s]["path"] = pathList.pop() + "/"
            sam[s]["sgeJobs"] = 80

    return sam
sam = icm(sam)
def fixLocalPaths(sam):
        import os,imp
        if "SmallXAnaDefFile" not in os.environ:
            print "Please set SmallXAnaDefFile environment variable:"
            print "export SmallXAnaDefFile=FullPathToFile"
            raise Exception("Whooops! SmallXAnaDefFile env var not defined")

        anaDefFile = os.environ["SmallXAnaDefFile"]
        mod_dir, filename = os.path.split(anaDefFile)
        mod, ext = os.path.splitext(filename)
        f, filename, desc = imp.find_module(mod, [mod_dir])
        mod = imp.load_module(mod, f, filename, desc)

        localBasePathPAT = mod.PATbasePATH
        localBasePathTrees = mod.TTreeBasePATH

        for s in sam:
            if "pathPAT" in sam[s]:
                sam[s]["pathPAT"] = sam[s]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            if "pathTrees" in sam[s]:
                sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            #print sam[s]["pathPAT"]
            #print sam[s]["pathTrees"]
        return sam
sam = fixLocalPaths(sam)
